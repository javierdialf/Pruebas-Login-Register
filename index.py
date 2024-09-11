#INDEX.PY
from app import app
from utils.db import db
from app import bcrypt;

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True);
    
bcrypt.init_app(app);