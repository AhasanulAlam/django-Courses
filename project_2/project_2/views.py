
from django.shortcuts import render


# D:\Phitron\Django\Django Codes\project_2\templates

def index(request):
    return render(request, 'index.html')