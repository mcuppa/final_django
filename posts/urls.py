from django.urls import path
from posts import views


urlpatterns = [
    path('articles/', views.articles, name='articles'),
   
   
    
]