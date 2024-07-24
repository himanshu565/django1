from django.shortcuts import render,HttpResponse 

# Create your views here.
def index(request):
    return HttpResponse("hello this is home page")

def about(request):
    return HttpResponse("hello this is about page")

def service(request):
    return HttpResponse("hello this is service page")

def contact(request):
    return HttpResponse(" this is contact page")