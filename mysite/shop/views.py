from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"index1.html")

def about(request):
    return render(request,"index1.html")

def contact(request):
    return render(request,"index1.html")

def tracker(request):
    return render(request,"index1.html")

def search(request):
    return render(request,"index1.html")

def prodview(request):
    return render(request,"index1.html")

def checkout(request):
    return render(request,"index1.html")
