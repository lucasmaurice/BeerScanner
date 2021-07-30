from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur', max_length=100)
    name = forms.CharField(label='Prénom/Surnom', max_length=100, required=False)
    tag_id = forms.CharField(label='Tag Unique ID', max_length=100) 
