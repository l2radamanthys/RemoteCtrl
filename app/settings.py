#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import bottle



HOST = "0.0.0.0"
PORT = 80
DEBUG = True

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC = '{}/media'.format(ROOT_PATH)

COMPUTER_CMD =  ROOT_PATH + "\\bin\\nircmdc.exe "
WINAMP_CMD =  ROOT_PATH + "\\bin\\clever.exe "

WINAMP_CMDS = [
    'next',
    'prev',
    'play',
    'current-song',
]