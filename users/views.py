from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login 
from django.contrib.auth.forms  import UserCreationForm


def register(request):
    if request.method == 'POST':
       form = RegistrationForm(request.POST)
     
       if form.is_valid():
           form.save()
           
           username = request.POST['username']
           password = request.POST['password1']
           user = authenticate(request, username=username, password = password)
           login(request, user)
           return redirect('blog-home')
    else:
        form = RegistrationForm()
    
    context = {'form':form }
    return render(request, 'users/register.html', context)



def Profile(request):
    args = {
        'user':request.user
    }
    return render(request, 'entries/profile.html' , args)











