from django import forms
from .models import MarvelModel


class MarvelForm(forms.ModelForm):

    class Meta:
        model = MarvelModel
        fields = ['name', 'heroic_name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'heroic_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter heroic name'})
        }
        
        # Customizing the labels for better design and styling
        labels = {
            'name': 'Avenger Name',
            'heroic_name': 'Heroic Name'
        }

    # Optional: You can further customize the fields with specific attributes (e.g., help texts, initial values)
    help_texts = {
        'name': 'Enter the name of the Avenger',
        'heroic_name': 'Enter the Avenger\'s heroic name'
    }