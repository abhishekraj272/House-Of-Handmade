from django.shortcuts import render
from .models import (Sweater,Sock,Scarf,Vase,Earring)

# Create your views here.
def login_page(request):
    return render(request,"login.html")

def signup_page(request):
    return render(request,"signup.html")

def sweaters_page(request):
    qs=Sweater.objects.all();
    context={"objectlist":qs}
    return render(request,"sweaters.html",context)

def earrings_page(request):
    qs=Earring.objects.all();
    context={"objectlist":qs}
    return render(request,"earrings.html",context)

def vases_page(request):
    qs=Vase.objects.all();
    context={"objectlist":qs}
    return render(request,"vases.html",context)

def scarfs_page(request):
    qs=Scarf.objects.all();
    context={"objectlist":qs}
    return render(request,"scarfs.html",context)

def socks_page(request):
    qs=Sock.objects.all();
    context={"objectlist":qs}
    return render(request,"socks.html",context)

def recover_page(request):
    return render(request,"recover.html")

def terms_page(request):
    return render(request,"termsandconditions.html")

def sweater_detail_page(request):
    return render(request,"sweater-details.html")

def vase_detail_page(request):
    return render(request,"vase-details.html")

def scarf_detail_page(request):
    return render(request,"scarfs-detail.html")

def socks_detail_page(request):
    return render(request,"socks-detail.html")

def earring_detail_page(request):
    return render(request,"earring-detail.html")
