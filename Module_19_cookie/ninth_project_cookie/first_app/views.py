from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse

# Create your views here.

def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name', 'Rahim')
    response.set_cookie('name', 'Mathew', max_age=10) # time in second eg 10 second
    # response.set_cookie('name', 'Mathew', expires=datetime.utcnow()+timedelta(days=3)) 
    return response


def get_cookie(request):
    name = request.COOKIES.get('name')
    return render(request, 'get_cookie.html', {'name' : name})


def delete_cookie(request):
    response = render(request, 'delete_cookie.html')
    response.delete_cookie('name')
    return response

def set_session(request):
    # data = {
    #     'name' : 'rahim',
    #     'age' : 23,
    #     'language' : 'Bangla',
    # }
    # print(request.session.get_session_cookie_age())
    # print(request.session.get_expiry_date())
    # request.session.update(data)
    request.session['name'] = 'Thomas'
    return render(request, 'home.html')

def get_session(request):
    # data = request.session
    # print(data)
    # return render(request,'get_session.html',{'data' : data})
    if 'name' in request.session:
        name = request.session.get('name', 'Guest')
        request.session.modified = True # reset the timer
        return render(request,'get_session.html',{'name' : name})
    else:
        return HttpResponse("Your Session has been Expired!!")
        


def delete_session(request):
    # del request.session['name'] # if delete only one data
    request.session.flush() # delete full data
    return render(request, 'delete_session.html')


