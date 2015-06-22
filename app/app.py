#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bottle
import views
from settings import *



#urls ruteo de aplicacion
urls = [
    ("/", ["GET"], views.index),
    ("", ["GET"], views.index),
    ("/pc/", ["GET"], views.computer),
    ("/pc-cmd/", ["POST"], views.computer_cmd),
    ("/winamp/", ["GET"], views.winamp),
    ("/winamp-cmd/", ["POST"], views.winamp_cmd),
    ("/winamp-current-song/", ["GET"], views.winamp_playing),
    ("/present/", ["GET"], views.present),
    #static
    ("/media/<filename:path>", ["GET"], views.static_),
]



def urls_routing(app):
    """
        Ruteo de Urls
    """
    for url in urls:
        app.route(url[0], url[1], url[2])



app = bottle.Bottle()
urls_routing(app)

bottle.debug(mode=DEBUG)
bottle.run(
        app=app,
        server='auto',
        host=HOST,
        quiet=not DEBUG, #show stderr and stdout in console
        port=PORT)