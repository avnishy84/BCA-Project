from django.urls import path , include
from . import views
urlpatterns = [
	path('',views.director,name='director'),    
   	path('dlogin',views.dlogin,name='dlogin'),    
    path('regis', views.regis,name='regis'),    
    path('regisact', views.regisact,name='regisact'),    
    path('logout', views.logout,name='logout'),    
    path('home', views.home,name='home'),    
    path('index', views.index,name='index'),    
    path('entries',views.entries,name='entries'),    
    path('delete',views.delete,name='delete'),    
    path('update_delete',views.update_delete,name='update_delete'),
]
