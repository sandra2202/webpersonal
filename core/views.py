from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Mi Web Personal Sandra</h1><h2>Portada</h2>")