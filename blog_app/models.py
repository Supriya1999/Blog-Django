from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

# choices = [('coding','coding'),('sports','sports'),('art','art')]

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog_app:home' , args=[self.slug])

choices = Category.objects.all().values_list('name','name')
choice_list=[]
for item in choices:
    choice_list.append(item)


class Blog(models.Model):

    title = models.CharField(max_length=200)
    header_image = models.ImageField(null=True,blank=True,upload_to="images/")
    description=RichTextField(blank=True,null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_app')
    category = models.CharField(max_length=200, choices=choice_list,default='coding')
    slug = models.SlugField(max_length=100,unique=True)
    updated=models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('blog_app:single' , args=[self.slug])

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title

