from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=55)
    content = models.TextField()
    category = models.ManyToManyField(Category) # One post might have multiple categories, and multiple posts might have in one category
    author = models.ForeignKey(User, on_delete=models.CASCADE)    # CASCADE will delete all the posts for this author 
    image = models.ImageField(upload_to='posts/media/uploads/', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) # Capture the time of created object

    def __str__(self):
        return f"Comments by {self.name}"
    