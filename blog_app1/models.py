from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime

# Entry - post  model

class Entry (models.Model):
    entry_title = models.CharField(max_length=50)
    entry_text = models.TextField()
    entry_date = models.DateTimeField(auto_now=True)
    
    entry_author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, default='0', related_name='likes', blank= True)
   

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f'{self.entry_title}'


#  Comment model 

class Com(models.Model):
    post = models.ForeignKey(Entry , on_delete=models.CASCADE ,  related_name='comments')
    user = models.CharField(max_length=30)
    content = models.TextField(max_length=160)
    created = models.DateTimeField( auto_now_add=True )
    approved_comment = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()


    def __str__(self):
        return self.content
   
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


    

 
  

    


