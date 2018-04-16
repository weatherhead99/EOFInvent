from flask import Flask
from webapp.config import Config
webapp = Flask(__name__)
webapp.config.from_object(Config)

from webapp import routes
