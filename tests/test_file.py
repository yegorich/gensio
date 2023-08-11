#
#  gensio - A library for abstracting stream I/O
#  Copyright (C) 2018  Corey Minyard <minyard@acm.org>
#
#  SPDX-License-Identifier: GPL-2.0-only
#

import utils
import gensio
import os

test1 = "asdfasdf"
test2 = "jkl;jkl;"
test3 = "01234;"

print("Test file")

try:
    os.remove("asdf")
except:
    pass

print(" Testing no create")
g = gensio.gensio(utils.o, "file(outfile=asdf)", None)
g.set_sync()
failed = False
try:
    g.open_s()
except Exception as e:
    if not str(e).endswith("Value or file not found"):
        raise Exception("Unknown exception opening file: " + str(e))
    failed = True
if not failed:
    raise Exception("Open didn't fail")
del g

def writefile(f, data, options = ""):
    g = gensio.gensio(utils.o, "file(outfile=%s%s)" % (f, options), None)
    g.set_sync()
    g.open_s()
    g.write_s(data, 1000)
    g.close_s()
    del g

def readfile(f, options = ""):
    g = gensio.gensio(utils.o, "file(infile=%s%s)" % (f, options), None)
    g.set_sync()
    g.open_s()
    s = g.read_s(100, 1000)
    g.close_s()
    del g
    s = s[0].decode('utf-8')
    return s
    
print(" Testing file data")
writefile("asdf", test1, ",create")
s = readfile("asdf")
if s != test1:
    raise Exception("file data didn't match, expected %s, got %s" % (
        test1, s))

print(" Testing append")
writefile("asdf", test2, ",append")
s = readfile("asdf")
if s != test1 + test2:
    raise Exception("file data didn't match, expected %s, got %s" % (
        test1 + test2, s))

print(" Testing overwrite")
writefile("asdf", test2)
s = readfile("asdf")
if s != test2 + test2:
    raise Exception("file data didn't match, expected %s, got %s" % (
        test2 + test2, s))

print(" Testing trunc")
writefile("asdf", test3, ",trunc")
s = readfile("asdf")
if s != test3:
    raise Exception("file data didn't match, expected %s, got %s" % (
        test3, s))

os.remove("asdf")

utils.test_shutdown()
print("  Success!")
