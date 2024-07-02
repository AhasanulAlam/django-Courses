from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView


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


# ADD POST USING CLASS BASED CREATEVIEW:
@method_decorator(login_required, name='dispatch')
class addPostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html' # Assigning the template
    success_url = reverse_lazy('add_post')   # redirect to the page 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

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


# UPDATE POST USING CLASS BASED UPDATEVIEW:
@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'  # Assigning the template
    pk_url_kwarg = 'id' # getting the id
    success_url = reverse_lazy('user_profile')   # redirect to the page 



@login_required
def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')  # redirect to the page 

# DELETE POST USING CLASS BASED DELETEVIEW:
@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'delete.html'  # Assigning the template
    pk_url_kwarg = 'id' # getting the id
    success_url = reverse_lazy('user_profile')   # redirect to the page 

# DETAILS POST USING CLASS BASED DETAILVIEW:
class DetailPostVied(DetailView):
    model = models.Post
    pk_url_kwarg = 'id' # getting the id
    template_name = 'post_details.html'
    


