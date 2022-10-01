from dataclasses import fields
import imp
from pyexpat import model
from django import forms
from .models import *
class postform(forms.ModelForm):
    class Meta:
        model=Post
        fields= fields=("title","content", )

        # 'img',