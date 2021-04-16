from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello there, globomantics e-commerce store front comming here...")


def detail(request):
    return HttpResponse("Hello there, globomantics e-commerce store front digital pages")


def eletronics(request):
    return HttpResponse("Hello there, globomantics eletronic front")