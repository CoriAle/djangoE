from django import forms
from .models import Publicacion

class PostForm(forms.ModelForm):
    """docstring fo PostForm."""
    class Meta:
        model = Publicacion
        fields = ('titulo', 'texto',)
