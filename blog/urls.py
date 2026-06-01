from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('blog-home/', blog_home, name='bolg-home'),
    path('blog-single/', blog_single, name='bolg-single')
]