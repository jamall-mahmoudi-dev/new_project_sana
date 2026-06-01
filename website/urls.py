from django.urls import path
from .views import *

app_name = 'website'

urlpatterns = [
    
    path('about/', about, name='about'),
    path('index/', index, name='index'),
    path('contact/', contact, name='contact'),
    path('test/', test, name='test'),
    path('sana/', sana, name='sana'),
    path('test_do/', test_do, name='test_do')
]