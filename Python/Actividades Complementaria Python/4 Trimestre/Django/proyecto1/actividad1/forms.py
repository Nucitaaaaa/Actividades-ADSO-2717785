
from django import forms
from django.core import validators

class FormArticulo(forms.Form):
    title = forms.CharField(
        label="Titulo",
        max_length=40,
        required=False,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'ingrese el titulo',
                'class': 'title_form_article'
            }
        ),
        validators= [
            validators.MinLengthValidator(4, 'El titulo es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9]*$','El titulo está mal escrito')
        ]
    )

    content = forms.CharField(
        label="contenido",
        max_length=40,
        required=False,
        widget = forms.Textarea(
            attrs = {
                'placeholder': 'ingrese el contenido',
                'class': 'contenido_form_article'
            }
        )
    )

    public_options = [(0, 'No'),(1, 'Si')]
    public = forms.TypedChoiceField(
        label = "Publicar?", 
        choices = public_options)
    
