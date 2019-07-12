from django.shortcuts import render

# Create your views here.
def login_page(request):
    return render(request,"login.html")

def signup_page(request):
    return render(request,"signup.html")

def sweaters_page(request):
    return render(request,"sweaters.html")

def earrings_page(request):
    return render(request,"earrings.html")

def vases_page(request):
    return render(request,"vases.html")

def scarfs_page(request):
    return render(request,"scarfs.html")

def socks_page(request):
    return render(request,"socks.html")
