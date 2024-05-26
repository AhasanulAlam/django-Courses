from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    d = {'author' : 'Rahim', 'age': 21, 'DOB' : datetime.datetime.now(), 'emptyValue': '' ,'list': ['Python','is','Best'], 'courses' : [
        {
            'id' : 1,
            'name' : 'Python',
            'fee' : 5000
        },
        {
            'id' : 2,
            'name' : 'Django',
            'fee' : 10000
        },
        {
            'id' : 3,
            'name' : 'JavaScript',
            'fee' : 3000
        },
    ]}
    return render(request, 'first_app/home.html', context=d)    # Context is sending the data from backend to frontend in dictionary form.