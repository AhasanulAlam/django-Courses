from django.db import models
from categories.models import Category
from author.models import Author

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=55)
    content = models.TextField()
    category = models.ManyToManyField(Category) # One post might have multiple categories, and multiple posts might have in one category
    author = models.ForeignKey(Author, on_delete=models.CASCADE)    # CASCADE will delete all the posts for this author 

    def __str__(self):
        return f'{self.title}'

