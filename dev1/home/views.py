from django.shortcuts import render,HttpResponse 
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    context = {
        "variable":"yoo its working"
    }
    return render(request,"index.html",context)
    # return HttpResponse("hello this is home page")

def about(request):
    return render(request,"about.html")
    # return HttpResponse("hello this is about page")

def service(request):
    return render(request,"services.html")
    # return HttpResponse("hello this is service page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,desc=desc)
        contact.save()
    return render(request,"contact.html")
    # return HttpResponse(" this is contact page")