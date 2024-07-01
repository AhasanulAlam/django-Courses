from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_post(request):
    if request.method =='POST': # user sent POST request
        post_form = forms.PostForm(request.POST)  # capture the user post data
        if post_form.is_valid(): # checking the post data validation
            # post_form.cleaned_data['author'] = request.user
            post_form.instance.author = request.user
            post_form.save() # if data valid save in the database
            return redirect('add_post')  # redirect to the page 
    else:
        post_form = forms.PostForm()  # user will get the blank form
    return render(request, 'add_post.html', {'form' : post_form})

@login_required
def edit_post(request, id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)

    if request.method =='POST': # user sent POST request
        post_form = forms.PostForm(request.POST, instance=post)  # capture the user post data
        if post_form.is_valid(): # checking the post data validation
            post_form.instance.author = request.user
            post_form.save() # if data valid save in the database
            return redirect('homepage')  # redirect to the page 
    return render(request, 'add_post.html', {'form' : post_form})

@login_required
def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')  # redirect to the page 

