#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 18:43:50 2016

@author: giovanni
"""

import os,sys
import stat


def changeMod(filename):
    st = os.stat(filename)
    os.chmod(filename, st.st_mode | stat.S_IEXEC|stat.S_IXUSR | stat.S_IXGRP|stat.S_IXOTH)


argv  = sys.argv
if len(argv) == 2:
    changeMod(argv[1])
else:
    print("U dient een bestandsnaam in te voeren")