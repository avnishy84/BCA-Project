"""entries URL Configuration"""

from django.urls import path, include
from . import views
urlpatterns = [
	path('',views.entries,name='entries'),
    
]