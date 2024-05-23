
from django.http import HttpResponse

def home(request):
    return HttpResponse('This is project main HOME page.')

def contact(request):
    return HttpResponse('This is project main CONTACT page.')
