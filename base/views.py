from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def list_pamong(request):
    return render(request, 'list-pamong.html')

def tambah_pamong(request):
    return render(request, 'tambah-pamong.html')