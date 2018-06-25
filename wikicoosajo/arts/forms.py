from django.forms import ModelForm
from django.views import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import articulo,categoria,Comentario
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ArticuloForm(ModelForm):
    class Meta:
        model = articulo
        fields = "__all__"
        exclude = ["fecha","validado","user"]

    def __init__(self, *args, **kwargs):
        super(ArticuloForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Agregar'))

class CatForm(ModelForm):
    class Meta:
        model = categoria
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CatForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Agregar'))

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']

    def __init__(self, *args, **kwargs):
        super(ComentarioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

class SignUpForm(UserCreationForm):
    nombre = form.CharField(max_length=30, required=False, help_text='Optional.')
    apellido = form.CharField(max_length=30,required=False, help_text='Optional')
    fecha_nac = form.DateField(help_text='Required. Format: DD-MM-YYYY')
    correo_coosajo = form.EmailField(max_length=254, help_text='Required. Correo electronico de Coosajo es necesario')

    class Meta:
        model: user
        fields ('username', 'nombre', 'apellido', 'correo_coosajo', 'fecha_nac', 'password1', 'password2', )
