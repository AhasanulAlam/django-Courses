from django.shortcuts import render, redirect
from posts.models import Post

# Create your views here.
def home(request):
    data = Post.objects.all()
    # print(data)
    # for i in data:
    #     print(i.title)
    #     for j in i.category.all():
    #         print(j)
    #     print()
    return render(request, 'home.html', {'data' : data})