from flask import Blueprint, request, jsonify
from models.User import User
from utils.db import db


users = Blueprint('users',__name__);

@users.route('/user_register', methods=['POST'])
def user_register():
    from app import bcrypt;
    full_name = request.json.get('Nombre')
    email_address = request.json.get('Email');
    password = request.json.get('Password');
    
    user_exits = User.query.filter_by(email_address=email_address).first() is not None
    
    if (user_exits):
        return 'El usuario ya existe',409;
    
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    new_user = User(full_name, email_address, hashed_password);
    db.session.add(new_user);
    db.session.commit();
    
    
    return 'se agrego bien, todo en orden',200;



@users.route('/user_login', methods=['POST'])
def user_login():
    from app import bcrypt;
    email_address = request.json.get('Email');
    password = request.json.get('Password');
    
    user = User.query.filter_by(email_address=email_address).first();
   
    if (user is None):
        return 'Error, no esta autenticado', 401;
    
    if (not bcrypt.check_password_hash(user.password, password)):
        return 'Error, no esta autenticado contra',401;
        
    return jsonify({
        "id":user.id,
        "email":user.email_address
    });


    


@users.route('/user_get', methods=['GET'])
def user_get():
    usuarios = User.query.all();
    todos_usuarios = [];
    for usuario in usuarios:
        todos_usuarios.append({
            'full_name': usuario.full_name,
            'email_address': usuario.email_address,
            'password': usuario.password
        })
    db.session.commit();
    return todos_usuarios;
    



@users.route('/user_delete/<id>', methods=['DELETE'])
def user_delete(id):
    user_eliminar = User.query.get(id)
    db.session.delete(user_eliminar);
    db.session.commit();
    return 'Eliminado yaaaaa',200;
    
    
    
    

    