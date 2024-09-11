#APP.PY
from flask import Flask
from routes.products import products
from utils.db import db
from routes.users import users;
from flask_bcrypt import Bcrypt;
from flask_cors import CORS
from config import CONEXION_DBA

bcrypt = Bcrypt();

app = Flask(__name__);
CORS(app);


#conexion
app.config['SQLALCHEMY_DATABASE_URI'] = CONEXION_DBA;
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False;
db.init_app(app)

#blueprints
app.register_blueprint(products);
app.register_blueprint(users);
