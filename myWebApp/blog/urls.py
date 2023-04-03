from django.urls import path
from . import views

# notes: 
# leave path blank for home page 
# views.home -> home view from views module

# path() syntax:
# path(route, view, kwargs = ___, name = ___)
# kwargs: allows you to pass additional arguments to the view 
# function/method

urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
]