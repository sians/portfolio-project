from django.shortcuts import render

def home(request):
    return render(request, 'projects/home.html')

def contact(request):
    return render(request, 'projects/contact.html')
