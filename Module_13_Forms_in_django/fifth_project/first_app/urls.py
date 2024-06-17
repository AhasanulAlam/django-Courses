from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'first_app_home_page'),
    path('about/', views.about, name= 'first_app_about_page'),
    path('form/', views.submit_form, name= 'first_app_form_page'),
    # path('django_form/', views.DjangoForm, name= 'django_form_page'),
    path('django_form/', views.StudentForm, name= 'django_form_page'),
]
