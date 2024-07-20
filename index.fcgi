#!/usr/bin/scl enable rh-python35 -- /homeX/CONTA/.virtualenv/bin/python
import os
import sys

from flup.server.fcgi import WSGIServer
from app import app  # Importa a aplicação Flask

sys.path.insert(0, "/home/cone0002/supermessenger-main")
os.environ['FLASK_APP'] = "app"

WSGIServer(app).run()
