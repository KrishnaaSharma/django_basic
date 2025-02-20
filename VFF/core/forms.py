from django import forms 

class MarvelForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        val_name = cleaned_data['name']
        val_password = cleaned_data['password']
        val_conpass = cleaned_data['confirm_password']

        if len(val_name)<5:
            raise forms.ValidationError('Please enter name more than 5 Letters')
        
        if val_password!=val_conpass:
            raise forms.ValidationError('Password doesn"t match')