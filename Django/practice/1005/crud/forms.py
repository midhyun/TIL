from django import forms
from django import forms
from .models import Crud

class CrudForm(forms.ModelForm):

    class Meta():
        model = Crud
        fields = ['title', 'content']