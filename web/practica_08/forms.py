from django import forms
from django.core.validators import RegexValidator
from .models import Album, Musico, Grupo
from django.db import models

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['titulo','distribuidora', 'fecha_lanzamiento', 'grupo']
        labels = {'distribuidora' : 'Nombre de la empresa distribuidora', 'fecha_lanzamiento' : 'Fecha de lanzamiento', 'grupo': 'A qué grupo pertenece'}
        validators = [RegexValidator(r'^\D+$', "Ningún campo puede empezar por dígito.")]

class MusicoForm(forms.ModelForm):
    class Meta:
        model = Musico
        fields = ['nombre', 'apellidos', 'fecha_nacimiento', 'instrumento_principal', 'grupos', 'ciudad', 'pais']
        labels = {'nombre' : 'Nombre del artista', 'fecha_nacimiento' : 'Fecha de nacimiento', 'instrumento_principal' : 'Instrumento principal', 'ciudad': 'Ciudad de natal', 'pais/estado natal (abreviado en dos letras)': 'País natal'}

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['nombre', 'fecha_fundacion', 'estilo', 'ciudad', 'pais']
        labels = {'ciudad': 'Ciudad donde se fundó', 'pais/estado (abreviado en dos letras)': 'País'}