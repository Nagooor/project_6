from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def sasi(request):
    return HttpResponse('<h1>this is sasi</h1>')

def siva(request):
    return HttpResponse('<h1>iam siva</h1>')