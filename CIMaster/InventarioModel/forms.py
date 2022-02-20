from django.forms import EmailField, Form,CharField, IntegerField,PasswordInput
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User


class ProductoForm(Form):
    nombre=CharField(max_length=70)
    descripcion = CharField(max_length=200)
    tipo = CharField(max_length=20)
    cantidad=IntegerField()
    
    
class UserRegistrationForm (UserCreationForm):
    
    email: EmailField(label= 'Email')

    password1: CharField(max_length=200, min_length=8, widget=PasswordInput, label='Contraseña')
    password2: CharField(max_length=200, min_length=8, widget=PasswordInput, label='Repetir Contraseña')
    
    class Meta:
        model = User
        fields = ['email','username','password1','password2']
        help_texts = {k:'' for k in fields}