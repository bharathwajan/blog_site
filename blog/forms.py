from django.db import models
from .models import comments
from django.forms import ModelForm
from django import forms

class commentform(ModelForm):
    class Meta:
        model=comments
        fields=('name','content','post')

        widgets={
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Your name here'}),
            'content' : forms.Textarea(attrs={'class':'form-control','rows':4, 'cols':107}),
            'post' : forms.Select(attrs={'class':'form-control'})
        }
    