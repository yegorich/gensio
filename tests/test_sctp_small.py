#
#  gensio - A library for abstracting stream I/O
#  Copyright (C) 2018  Corey Minyard <minyard@acm.org>
#
#  SPDX-License-Identifier: GPL-2.0-only
#

from utils import *
import gensio

print("Test sctp small")
ta = TestAccept(o, "sctp,localhost,", "sctp,0", do_small_test, chunksize = 64)
