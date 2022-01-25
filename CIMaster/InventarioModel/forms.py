from email.policy import default
from enum import unique
from django.forms import Form,CharField, IntegerField

class ProductoForm(Form):
    nombre=CharField(max_length=70)
    descripcion = CharField(max_length=200)
    tipo = CharField(max_length=20)
    cantidad=IntegerField()
    
    