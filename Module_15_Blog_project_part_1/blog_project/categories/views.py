from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def add_category(request):
    if request.method =='POST': # user sent POST request
        category_form = forms.CategoryForm(request.POST)  # capture the user post data
        if category_form.is_valid(): # checking the post data validation
            category_form.save() # if data valid save in the database
            return redirect('add_category')  # redirect to the page 
    else:
        category_form = forms.CategoryForm()  # user will get the blank form
    return render(request, 'add_category.html', {'form' : category_form})