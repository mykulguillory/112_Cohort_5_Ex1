from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# We create fns that takes the request from the user
# and emits a response

def index(request):
    return HttpResponse("Hello world")

def test(request):
    return HttpResponse("This is a test page!")

def developer(request):
    return HttpResponse("<h1>Mykul Guillory</h1>")
