
from django import forms 
from django.contrib.auth.models import User
from .models import Com




class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []


class CommentForm(forms.ModelForm):
    class Meta:
        model = Com
        fields = ('content', 'user', )

        