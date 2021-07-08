from django.shortcuts import render

# Create your views here.

def pag_home(request):
    return render(request, 'index.html', {})
