from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

from app import views
from app import Calif_Actinver
