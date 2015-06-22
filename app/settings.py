#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import bottle



HOST = "0.0.0.0"
PORT = 8080
DEBUG = True

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC = '{}/media'.format(ROOT_PATH)