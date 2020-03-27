from django.shortcuts import render ,get_object_or_404 , redirect , HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Entry
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django import forms
from .forms import UserDeleteForm ,CommentForm 
from .models import *





class HomeView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'entries/index.html'
    context_object_name = 'blog_entries'
    paginate_by = 3

class EntryView(LoginRequiredMixin, DetailView):
    model = Entry
    
    template_name = 'entries/entry_detail.html'
    
  
class CreateEntryView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = 'entries/create_entry.html'
    fields = ['entry_title', 'entry_text']

    def form_valid (self,form):
        form.instance.entry_author = self.request.user
        return super().form_valid(form)





def Profile(request ):

    
    
    return render(request, 'entries/profile.html')









def like_post(request , pk):

    post = get_object_or_404(Entry, id=request.POST.get('entry_id') , pk=pk)
    is_liked = False
    if post.likes.filter(id=request.user.id ).exists():


        post.likes.remove(request.user)

        is_liked = False
    else:


        post.likes.add(request.user)
        is_liked = True

    return redirect('entry-detail' , pk=post.id)



def deleteuser(request):
    if request.method == 'POST':
        delete_form = UserDeleteForm(request.POST , instance = request.user)
        user = request.user
        user.delete()
        messages.info(request, 'Your account has been deleted !')
        return redirect('blog-home')
    else:
        delete_form = UserDeleteForm(instance =request.user )
    context = {
        'delete_form': delete_form

    }
    return render(request, 'entries/delete_profile.html' , context)



def add_comment(request , pk):
    post = get_object_or_404(Entry, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('entry-detail' , pk= post.pk )
    else:
        form = CommentForm()
    template = 'entries/add_comment.html'
    context = {'form': form}
    return render(request, template, context)
    





