from django import forms

class RegistrarLibros(forms.Form):
    titulo = forms.CharField(max_length=30)
    autor = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=40)
    disponible = forms.BooleanField(default=False)
    fecha = forms.DateTimeField()
    cantidad = forms.IntegerField()