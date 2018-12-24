#
# gensio test utilities
#
# This file contains some classes and functions useful for testing
# gensio handling
#

import os
import gensio
import tempfile
import signal
import time
import curses.ascii
import sys

debug = 0

class HandlerException(Exception):
    """Exception for HandleData errors"""

    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return repr(self.value)
    def __str__(self):
        return str(self.value)

class HandleData:
    """Data handler for testing gensio.

    This is designed to handle input and output from gensio.  To write
    data, call set_write_data() to set some data and write it.  To wait
    for data to be read, call set_compare() to wait for the given data
    to be read.

    This just starts things up and runs asynchronously.  You can wait
    for a completion with wait() or wait_timeout().

    The io handler is in the io attribute of the object.  The handler
    object of that io will be this object.
    """

    def __init__(self, o, iostr, name = None, chunksize=10240,
                 io = None):
        """Start a gensio object with this handler"""
        if (name):
            self.name = name
        else:
            self.name = iostr
        self.waiter = gensio.waiter(o)
        self.to_write = None
        self.to_compare = None
        self.to_waitfor = None
        self.expecting_modemstate = False
        self.expecting_linestate = False
        self.expected_server_cb = None
        self.expected_server_value = 0
        self.expected_server_return = 0
        self.ignore_input = False
        if (io):
            self.io = io
            io.set_cbs(self)
        else:
            self.io = gensio.gensio(o, iostr, self)
        self.io.handler = self
        self.chunksize = chunksize
        self.debug = 0
        return

    def set_compare(self, to_compare, start_reader = True):
        """Set some data to compare

        If start_reader is true (default), it enable the read callback.
        If the data does not compare, an exception is raised.
        """
        self.compared = 0
        self.to_compare = to_compare
        if (start_reader):
            self.io.read_cb_enable(True)
        return

    def set_waitfor(self, waitfor, start_reader = True):
        """Wait for the given string to come in

        If start_reader is true (default), it enable the read callback.
        If the data does not compare, an exception is raised.
        """
        self.compared = 0
        self.to_waitfor = waitfor
        if (start_reader):
            self.io.read_cb_enable(True)
        return

    def set_write_data(self, to_write, start_writer = True,
                       close_on_done = False):
        self.close_on_done = close_on_done
        self.wrpos = 0
        self.wrlen = len(to_write)
        self.to_write = to_write
        if (start_writer):
            self.io.write_cb_enable(True)
        return

    def close(self):
        self.ignore_input = True
        self.io.close(self)
        return

    def wait(self):
        self.waiter.wait(1)

    def wait_timeout(self, timeout):
        return self.waiter.wait_timeout(1, timeout)


    # Everything below here is internal handling functions.

    def read_callback(self, io, err, buf, auxdata):
        if self.to_compare:
            iolen = len(self.to_compare)
        elif self.to_waitfor:
            iolen = len(self.to_waitfor)
        else:
            iolen = None

        if (debug or self.debug) and iolen != None:
            print("%s: Got %d bytes at pos %d of %d" % (self.name, len(buf),
                                                        self.compared, iolen))
        if (debug >= 2 or self.debug >= 2):
            s = ""
            for i in buf:
                if curses.ascii.isprint(i):
                    s = s + i
                else:
                    s = s + "\\x%2.2x" % ord(i)
            print("%s: Got data: (err %s %d bytes) %s" % (self.name, str(err),
                                                          len(buf), s))
        if (err):
            raise HandlerException(self.name + ": read: " + err)
        if (self.ignore_input):
            return len(buf)
        if (self.to_waitfor):
            for i in range(0, len(buf)):
                if buf[i] == self.to_waitfor[self.compared]:
                    self.compared += 1
                    if (len(self.to_waitfor) == self.compared):
                        self.to_waitfor = None
                        io.read_cb_enable(False)
                        self.waiter.wake()
                else:
                    self.compared = 0
            return len(buf)

        if (not self.to_compare):
            if (debug):
                print(self.name + ": Got data, but nothing to compare")
            io.read_cb_enable(False)
            return len(buf)

        if (len(buf) > len(self.to_compare)):
            count = len(self.to_compare)
        else:
            count = len(buf)

        if count > self.chunksize:
            count = self.chunksize

        for i in range(0, count):
            if (buf[i] != self.to_compare[self.compared]):
                raise HandlerException("%s: compare failure on byte %d, "
                                       "expected %x, got %x" %
                                       (self.name, self.compared,
                                        ord(self.to_compare[self.compared]),
                                        ord(buf[i])))
            self.compared += 1

        if (self.compared >= len(self.to_compare)):
            self.to_compare = None
            io.read_cb_enable(False)
            self.waiter.wake()

        return count

    def write_callback(self, io):
        if (not self.to_write):
            if (debug or self.debug):
                print(self.name + ": Got write, but no data")
            io.write_cb_enable(False)
            return

        if (self.wrpos + self.chunksize > self.wrlen):
            wrdata = self.to_write[self.wrpos:]
        else:
            wrdata = self.to_write[self.wrpos:self.wrpos + self.chunksize]
        count = io.write(wrdata, None)
        if (debug or self.debug):
            print(self.name + ": wrote %d bytes" % count)

        if (count + self.wrpos >= self.wrlen):
            io.write_cb_enable(False)
            if (self.close_on_done):
                self.io.closeme = False
                self.close()
            self.to_write = None
            self.waiter.wake()
        else:
            self.wrpos += count
        return

    def urgent_callback(self, io):
        print(self.name + ": Urgent data")
        return

    def modemstate(self, io, modemstate):
        if (not self.expecting_modemstate):
            if (debug or self.debug):
                print("Got unexpected modemstate for %s: %x" %
                      (self.name, modemstate))
            return
        if (modemstate != self.expected_modemstate):
            raise HandlerException("%s: Expecting modemstate 0x%x, got 0x%x" %
                                   (self.name, self.expected_modemstate,
                                    modemstate))
        self.expecting_modemstate = False
        self.waiter.wake()
        return

    def set_expected_modemstate(self, modemstate):
        self.expecting_modemstate = True
        self.expected_modemstate = modemstate
        return

    def linestate(self, io, linestate):
        if (not self.expecting_linestate):
            if (debug or self.debug):
                print("Got unexpected linestate %x" % linestate)
            return
        if (linestate != self.expected_linestate):
            raise HandlerException("%s: Expecting linestate 0x%x, got 0x%x" %
                                   (self.name, self.expected_linestate,
                                    linestate))
        self.expecting_linestate = False
        self.waiter.wake()
        return

    def set_expected_linestate(self, linestate):
        self.expecting_linestate = True
        self.expected_linestate = linestate
        return

    def set_expected_server_cb(self, name, value, retval):
        self.expected_server_cb = name
        self.expected_server_value = value
        self.expected_server_return = retval
        return

    def set_expected_client_cb(self, name, value):
        self.expected_server_cb = name
        self.expected_server_value = value
        return

    def check_set_expected_telnet_cb(self, name, value):
        if not self.expected_server_cb:
            if (debug or self.debug):
                print("Got unexpected server cb: %s %d" % (name, value))
            return False
        if self.expected_server_cb != name:
            raise HandlerException(
                "Got wrong server cb, expected %s, got %s (%d)" %
                (self.expected_server_cb, name, value))
        if self.expected_server_value != value:
            raise HandlerException(
                "Got wrong server cb value for %s, expected %d, got %d" %
                (name, self.expected_server_value, value))
        self.waiter.wake()
        return True

    def baud(self, sio, err, baud):
        if not self.check_set_expected_telnet_cb("baud", baud):
            return
        return

    def datasize(self, sio, err, datasize):
        if not self.check_set_expected_telnet_cb("datasize", datasize):
            return
        return

    def parity(self, sio, err, parity):
        if not self.check_set_expected_telnet_cb("parity", parity):
            return
        return

    def stopbits(self, sio, err, stopbits):
        if not self.check_set_expected_telnet_cb("stopbits", stopbits):
            return
        return

    def flowcontrol(self, sio, err, flowcontrol):
        if not self.check_set_expected_telnet_cb("flowcontrol", flowcontrol):
            return
        return

    def iflowcontrol(self, sio, err, iflowcontrol):
        if not self.check_set_expected_telnet_cb("iflowcontrol", iflowcontrol):
            return
        return

    def sbreak(self, sio, err, sbreak):
        if not self.check_set_expected_telnet_cb("sbreak", sbreak):
            return
        return

    def dtr(self, sio, err, dtr):
        if not self.check_set_expected_telnet_cb("dtr", dtr):
            return
        return

    def rts(self, sio, err, rts):
        if not self.check_set_expected_telnet_cb("rts", rts):
            return
        return

    def sbaud(self, sio, baud):
        if not self.check_set_expected_telnet_cb("baud", baud):
            return
        sio.sg_baud(self.expected_server_return, None)
        return

    def sdatasize(self, sio, datasize):
        if not self.check_set_expected_telnet_cb("datasize", datasize):
            return
        sio.sg_datasize(self.expected_server_return, None)
        return

    def sparity(self, sio, parity):
        if not self.check_set_expected_telnet_cb("parity", parity):
            return
        sio.sg_parity(self.expected_server_return, None)
        return

    def sstopbits(self, sio, stopbits):
        if not self.check_set_expected_telnet_cb("stopbits", stopbits):
            return
        sio.sg_stopbits(self.expected_server_return, None)
        return

    def sflowcontrol(self, sio, flowcontrol):
        if not self.check_set_expected_telnet_cb("flowcontrol", flowcontrol):
            return
        sio.sg_flowcontrol(self.expected_server_return, None)
        return

    def siflowcontrol(self, sio, iflowcontrol):
        if not self.check_set_expected_telnet_cb("iflowcontrol", iflowcontrol):
            return
        sio.sg_iflowcontrol(self.expected_server_return, None)
        return

    def ssbreak(self, sio, sbreak):
        if not self.check_set_expected_telnet_cb("sbreak", sbreak):
            return
        sio.sg_sbreak(self.expected_server_return, None)
        return

    def sdtr(self, sio, dtr):
        if not self.check_set_expected_telnet_cb("dtr", dtr):
            return
        sio.sg_dtr(self.expected_server_return, None)
        return

    def srts(self, sio, rts):
        if not self.check_set_expected_telnet_cb("rts", rts):
            return
        sio.sg_rts(self.expected_server_return, None)
        return

    def close_done(self, io):
        if (debug or self.debug):
            print(self.name + ": Closed")
        self.waiter.wake()
        return

def alloc_io(o, iostr, do_open = True, chunksize = 10240):
    """Allocate an io instance with a HandlerData handler

    If do_open is True (default), open it, too.
    """
    h = HandleData(o, iostr, chunksize = chunksize)
    if (do_open):
        h.io.open_s()
    return h.io

def test_dataxfer(io1, io2, data, timeout = 1000):
    """Test a transfer of data from io1 to io2

    If the transfer does not complete by "timeout" milliseconds, raise
    an exception.
    """
    io1.handler.set_write_data(data)
    io2.handler.set_compare(data)
    if (io1.handler.wait_timeout(timeout)):
        raise Exception(("%s: %s: " % ("test_dataxfer", io1.handler.name)) +

                        ("Timed out waiting for write completion at byte %d" %
                         io1.handler.wrpos))
    if (io2.handler.wait_timeout(timeout)):
        raise Exception(("%s: %s: " % ("test_dataxfer", io2.handler.name)) +

                        ("Timed out waiting for read completion at byte %d" %
                         io2.handler.compared))
    return

def test_dataxfer_simul(io1, io2, data, timeout = 10000):
    """Test a simultaneous bidirectional transfer of data between io1 to io2

    If the transfer does not complete by "timeout" milliseconds, raise
    an exception.
    """
    io1.handler.set_write_data(data)
    io1.handler.set_compare(data)
    io2.handler.set_write_data(data)
    io2.handler.set_compare(data)
    if (io1.handler.wait_timeout(timeout)):
        raise Exception("%s: %s: Timed out waiting for write completion" %
                        ("test_dataxfer", io1.handler.name))
    if (io2.handler.wait_timeout(timeout)):
        raise Exception("%s: %s: Timed out waiting for write completion" %
                        ("test_dataxfer", io2.handler.name))
    if (io1.handler.wait_timeout(timeout)):
        raise Exception("%s: %s: Timed out waiting for read completion" %
                        ("test_dataxfer", io1.handler.name))
    if (io2.handler.wait_timeout(timeout)):
        raise Exception("%s: %s: Timed out waiting for read completion" %
                        ("test_dataxfer", io2.handler.name))
    return

def test_write_drain(io1, io2, data, timeout = 1000):
    """Test that a close does not loose data.

    If the transfer does not complete by "timeout" milliseconds, raise
    an exception.
    """
    io1.handler.set_write_data(data, close_on_done = True)
    io2.handler.set_compare(data)
    if (io1.handler.wait_timeout(timeout)):
        raise Exception(("%s: %s: " % ("test_dataxfer", io1.handler.name)) +
                        ("Timed out waiting for write completion at byte %d" %
                         io1.handler.wrpos))
    if (io2.handler.wait_timeout(timeout)):
        raise Exception(("%s: %s: " % ("test_dataxfer", io2.handler.name)) +
                        ("Timed out waiting for read completion at byte %d" %
                         io2.handler.compared))
    return

def io_close(io, timeout = 1000):
    """close the given gensio

    If it does not succeed in timeout milliseconds, raise and exception.
    """
    io.handler.close()
    if (io.handler.wait_timeout(timeout)):
        raise Exception("%s: %s: Timed out waiting for close" %
                        ("io_close", io.handler.name))
    return

srcdir = os.getenv("srcdir")
if not srcdir:
    srcdir = os.path.dirname(sys.argv[0])
    if (not srcdir):
        srcdir = "."
