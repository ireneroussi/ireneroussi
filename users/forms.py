from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 




class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name= forms.CharField()

    

    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'password1','password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.last_name = self.cleaned_data['last_name']
        user.first_name = self.cleaned_data['first_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user







