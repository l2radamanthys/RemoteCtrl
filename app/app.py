#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bottle
import views
from settings import *



#urls ruteo de aplicacion
urls = [
    ("/", ["GET"], views.index),
    ("/winamp/", ["GET"], views.winamp),
    ("/winamp-cmd/", ["POST"], views.winamp_cmd),

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
        #app=StripPathMiddleware(app),
        server='auto',
        host=HOST,
        quiet=not DEBUG, #show stderr and stdout in console
        port=PORT)