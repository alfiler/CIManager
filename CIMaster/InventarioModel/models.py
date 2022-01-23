from pydoc import describe
from django.db import models

from django.db.models import Model
from django.db.models.fields import CharField,IntegerField


# Create your models here.


class Producto (Model): 
    nombre = CharField(max_length=50)
    descripcion = CharField(max_length=50)
    tipo = CharField(max_length=50)
    cantidad = IntegerField(default=0)


        
    