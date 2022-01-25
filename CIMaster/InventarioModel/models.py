from pydoc import describe
from django.db import models

from django.db.models import Model
from django.db.models.fields import CharField,IntegerField


# Create your models here.


class Producto (Model): 
    nombre = CharField(max_length=70)
    descripcion = CharField(max_length=200)
    tipo = CharField(max_length=20)
    cantidad = IntegerField()
    
    def __str__(self):
        return f'Producto: {self.nombre} - Descripcion: {self.descripcion} - Tipo: {self.tipo} - Cantidades: {self.cantidad}'



        
    