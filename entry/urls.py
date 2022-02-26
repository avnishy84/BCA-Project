"""entry URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
	path('',views.index,name='index'),
    path('director/',include('director.urls')),
    path('gaurd/',include('gaurd.urls')),
    #path('entries/',include('entries.urls')),
    path('admin/', admin.site.urls),
    
]