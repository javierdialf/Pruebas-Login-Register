#PRODUCTS.PY
from utils.db import db;

class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True);
    codigo_producto = db.Column(db.String(6), nullable=False);
    nombre = db.Column(db.String(50));
    stok = db.Column(db.Integer);
    precio_unitario = db.Column(db.Float);
    tipo_producto = db.Column(db.String(20));
    descripcion = db.Column(db.String(100));
    calificacion_producto = db.Column(db.Integer);
    imagenes_producto = db.Column(db.LargeBinary(length=(2**32)-1))
    
    
    def __init__(self, codigo_producto,nombre,stok,precio_unitario,tipo_producto,descripcion,calificacion_producto,imagenes_producto):
        self.codigo_producto = codigo_producto;
        self.nombre = nombre;
        self.stok = stok;
        self.precio_unitario = precio_unitario;
        self.tipo_producto = tipo_producto;
        self.descripcion = descripcion;
        self.calificacion_producto = calificacion_producto;
        self.imagenes_producto = imagenes_producto;
        
