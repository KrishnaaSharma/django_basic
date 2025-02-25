from django import forms
from .models import MarvelModel, DcModel


# class MarvelForm(forms.Form):
#     name = forms.CharField()
#     heroic_name = forms.CharField()

class MarvelForm(forms.ModelForm):

    class Meta:
        model = MarvelModel
        fields = ['name', 'heroic_name']


class DcForm(forms.ModelForm):

    class Meta:
        model = DcModel
        fields= ['name','heroic_name']