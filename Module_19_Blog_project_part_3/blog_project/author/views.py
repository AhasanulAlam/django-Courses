from typing import Any
from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.
# def add_author(request):
#     if request.method =='POST':
#         author_form = forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect('add_author')
#     else:
#         author_form = forms.AuthorForm()
#     return render(request, 'add_author.html', {'form' : author_form})

def register(request):
    if request.method =='POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'User Account Created Successfully!')
            return redirect('register')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form' : register_form, 'type' : 'Register'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, 'User Logged In Successfully!')
                login(request, user)
                return redirect('user_profile')
            else:
                messages.warning(request, 'Login Information incorrect!')
                return redirect('register')
    else:
        form = AuthenticationForm()
        return render(request, 'register.html', {'form' : form, 'type' : 'Login'})

# LOGIN USING CLASS BASED LOGINVIEW:
class UserLoginView(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy('user_profile')
    def get_success_url(self):
        return reverse_lazy('user_profile')
    def form_valid(self, form):
        messages.success(self.request, 'User Logged In Successfully!')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'Incorrect Logged In Information!')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context


@login_required
def user_profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, './profile.html', {'data' : data, 'type' : 'Profile'})


@login_required
def edit_profile(request):
    if request.method =='POST':
        profile_form = forms.changeUserDataForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated Successfully!')
            return redirect('user_profile')
    else:
        profile_form = forms.changeUserDataForm(instance = request.user)
    return render(request, './update_profile.html', {'form' : profile_form, 'type' : 'Edit Profile'})


@login_required
def pass_change(request):
    if request.method =='POST':
        pass_change_form = PasswordChangeForm(request.user, data = request.POST)
        if pass_change_form.is_valid():
            pass_change_form.save()
            messages.success(request, 'Password Updated Successfully!')
            update_session_auth_hash(request, pass_change_form.user)
            return redirect('user_profile')
    else:
        pass_change_form = PasswordChangeForm(user = request.user)
    return render(request, './pass_change.html', {'form' : pass_change_form, 'type' : 'Password Change'})


def user_logout(request):
    logout(request)
    return redirect('homepage')


# LOGOUT USING CLASS BASED LOGOUTVIEW:
class UserLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('homepage')
    