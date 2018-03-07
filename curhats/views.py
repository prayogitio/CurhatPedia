from django.shortcuts import render, redirect

# Create your views here.
def curhat_list(request):
    return render(request, 'curhats/curhat_page.html')