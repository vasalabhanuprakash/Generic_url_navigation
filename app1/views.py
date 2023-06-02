from django.shortcuts import render

# Create your views here.

def bahubali(request):
    return render(request,'bahubali.html')

def saaho(request):
    return render(request, 'saaho.html')