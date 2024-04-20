from django.urls import path
from users import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('salir/', views.salir, name='salir'),
    path('home/',views.home,name='home'),
    path('edit', views.edit_profile, name='profile_edit'),
   
    
]