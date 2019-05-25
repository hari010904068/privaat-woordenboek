from flask import Flask
import os

# https://lepture.com/en/2018/structure-of-a-flask-project

app = Flask(__name__)
app.config.from_mapping(
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
) 

from flaskr import db
db.init_app(app)

import flaskr.routes