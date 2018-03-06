from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'index.html')