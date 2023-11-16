from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def virat(request):
    return HttpResponse('<h1>this is virat kohli</h1>')

def msd(request):
    return HttpResponse('<h1>iam ms dhoni</h1>')