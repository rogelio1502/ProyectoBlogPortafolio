from django.db import models
from django.shortcuts import reverse,redirect

from django.shortcuts import get_object_or_404
# Create your models here.

from usuario.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField(null=True,upload_to="posts/")
    publish_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    slug = models.SlugField()
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail",kwargs={
            "slug":self.slug
        })
    def get_like_url(self):
        return reverse("like",kwargs={
            "slug":self.slug
        })
    def get_like_url_detail(self):
        return reverse("like_detail",kwargs={
            "slug":self.slug
        })
    
    
    @property
    def comments(self):
        return self.comment_set.all()
    @property
    def get_comment_count(self):
        return self.comment_set.all().count()
    @property
    def get_view_count(self):
        return self.postview_set.all().count()
    @property
    def get_like_count(self):
        return self.like_set.all().count()



class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(verbose_name="Expresate")

    def __str__(self):
        return self.user.username
    
class PostView(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    user_2 = models.CharField(max_length=7,null=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    




    
