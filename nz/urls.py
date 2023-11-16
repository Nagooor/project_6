from nz.views import *
from django.urls import path
app_name='bramha'
urlpatterns=[
    path('sasi/',sasi,name='sasi'),
    path('siva/',siva,name='siva'),
]