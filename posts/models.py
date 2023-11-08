from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User





class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=20000)
    draft = models.BooleanField(default=True)
    publish_date= models.DateTimeField(default = timezone.now)
    tags = TaggableManager()
    imag=models.ImageField(upload_to='post')
    author = models.ForeignKey(User,related_name='post_author',on_delete=models.CASCADE)





    def __str__(self):
        return self.title