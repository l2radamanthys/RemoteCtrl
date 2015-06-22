#!/usr/bin/env python
# -*- coding: utf-8 -*-


import bottle
from bottle import template, request, response
import os
import sys
from settings import *


def index():
    return template("index.html")



def winamp():
    return template("winamp.html")



def winamp_cmd():
    cmd = request.forms.get('cmd')
    command = "{}\\bin\\clever.exe {}".format(ROOT_PATH, cmd)
    print command
    os.system(command)



def static_(filename):
    """
        Servir archivos estaticos
    """
    return bottle.static_file(filename, root=STATIC)