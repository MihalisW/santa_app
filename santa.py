from http_layer import app
from config import Config
from http_layer import routes

app.config.from_object(Config)