from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,"home_page.html")

def sweaters_page(request):
    return render(request,"sweaters.html")

def login_page(request):
    return render(request,"login.html")

def signup_page(request):
    return render(request,"register.html")

def recover_page(request):
    return render(request,"recover_pass.html")