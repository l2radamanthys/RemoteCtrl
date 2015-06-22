#!/usr/bin/env python
# -*- coding: utf-8 -*-


import bottle
from bottle import template, request, response
import os
import sys
from libs.comands import wnpcmd
from settings import *


def index():
    return template("home.html")



def computer():
    return template("desktop.html")



def computer_cmd():
    """
    """
    cmd = request.forms.get('cmd')
    command = COMPUTER_CMD + cmd
    os.system(command)
    print command



def present():
    return template("present.html")



def winamp():
    return template("winamp.html")



def winamp_cmd():
    """
    """
    cmd = request.forms.get('cmd')
    if cmd in WINAMP_CMDS:
        wnpcmd(cmd)
        #print cmd

    else:
        #command = "{}\\bin\\clever.exe {}".format(ROOT_PATH, cmd)
        command = WINAMP_CMD + cmd
        os.system(command)
        #print command



def winamp_playing():
    """
        Retorna el titulo de la cancion que suena en winamp
    """
    song = wnpcmd('current-song')
    if song == "":
        song = "----------------------"
    return song



def static_(filename):
    """
        Servir archivos estaticos
    """
    return bottle.static_file(filename, root=STATIC)