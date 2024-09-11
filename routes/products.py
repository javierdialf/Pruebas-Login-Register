from flask import Blueprint,request,jsonify
from models.Product import Product;
from utils.db import db

products = Blueprint('products',__name__);

@products.route('/')
def Home():
    return 'hello, here is a home';

@products.route('/product_create', methods=['POST'])
def add_product():
    codigo_producto = request.form['codigo']
    nombre = request.form['nombre']
    stok = request.form['stok']
    precio_unitario = request.form['precio']
    tipo_producto = request.form['tipo']
    descripcion = request.form['descripcion']
    calificacion_producto = request.form['calificacion']
    imagenes_producto = request.files['imagenes'];
    
    if not imagenes_producto:
        return 'Sube la imagen que no subiste nada',400;
    
    imagenes = imagenes_producto.read();
    
    new_product = Product(codigo_producto,nombre,stok,precio_unitario,tipo_producto,descripcion,calificacion_producto,imagenes)
    db.session.add(new_product)
    db.session.commit()
    return 'hola, se agrego Bien',200;


@products.route('/product_getAll', methods=['GET'])
def get_products():
    productos = Product.query.all()
    todos_productos = []
    for producto in productos:
       todos_productos.append({
           'codigo_producto': producto.codigo_producto,
            'nombre': producto.nombre,
            'stok': producto.stok,
            'precio_unitario': producto.precio_unitario,
            'tipo_producto': producto.tipo_producto,
            'descripcion': producto.descripcion,
            'calificacion_producto': producto.calificacion_producto,
            'imagenes_producto': producto.imagenes_producto
       })
       
       db.session.commit();
    return 'registro en la base de datos = ' + str(len(todos_productos));




@products.route('/product_delete/<id>', methods=['DELETE'])
def delete_product(id):
    producto_eliminar = Product.query.get(id)
    db.session.delete(producto_eliminar)
    db.session.commit()
    
    return 'Eliminado ya',200

