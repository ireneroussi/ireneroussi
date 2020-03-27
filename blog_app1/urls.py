from django.urls import path

from .views import HomeView, EntryView, CreateEntryView 
from . import views

urlpatterns = [
    
    
    path('', HomeView.as_view(), name='blog-home' ),
    path('entry/<int:pk>/', EntryView.as_view(), name='entry-detail' ),
    path('create_entry/', CreateEntryView.as_view(success_url='/'), name='create-entry' ),
    path('profile/', views.Profile , name='profile' ),
    path('delete_profile/', views.deleteuser , name='delete_profile' ),
    path('like/<int:pk>', views.like_post, name='like_post'),
    path('comment/<int:pk>/', views.add_comment , name='add_comment'),
    
]