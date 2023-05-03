from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('student/', students, name='student'),
    path('registration/', registration, name='reg'),
]
