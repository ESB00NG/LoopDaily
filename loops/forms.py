from django import forms
from .models import Loop
from .models import Comment
from .models import UserProfile

# Formulario para el modelo Loop
class LoopForm(forms.ModelForm):
    class Meta:
        model = Loop  # Especifica que el formulario corresponde al modelo Loop
        fields = ['title', 'description', 'bpm', 'escala', 'categoria', 'file', 'image']  # Campos que serán incluidos en el formulario

# Formulario para el modelo Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # Especifica que el formulario corresponde al modelo Comment
        fields = ['text']  # Campo que será incluido en el formulario
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Escribe tu comentario aquí...'}),  # Personalización del campo de texto, incluyendo clases CSS y atributos HTML
        }

# Formulario para el modelo UserProfile
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # Especifica que el formulario corresponde al modelo UserProfile
        fields = ['profile_picture']  # Campo que será incluido en el formulario, permite al usuario subir una imagen de perfil
