from pydoc import describe
from django.db import models

from django.db.models import Model
from django.db.models.fields import CharField,IntegerField,DecimalField




# Create your models here.


class Producto (Model): 
    nombre = CharField(max_length=70)
    descripcion = CharField(max_length=200)
    tipo = CharField(max_length=20)
    cantidad = IntegerField()
    
    def __str__(self):
        return f'Producto: {self.nombre} - Descripcion: {self.descripcion} - Tipo: {self.tipo} - Cantidades: {self.cantidad}'


class Ventas (Model):
    nombre_producto = CharField(max_length=70)
    precio_producto = DecimalField(max_digits=5,decimal_places=2)
    vendedor_id = IntegerField()
    cantidades = IntegerField()
    
    def __str__(self):
        return f'Producto: {self.nombre_producto} - Precio: {self.precio_producto} - Vendedor Id: {self.vendedor_id} - Cantidades: {self.cantidades}'

    
    