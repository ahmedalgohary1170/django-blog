from django.db import models






class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=20000)
    draft = models.BooleanField(default=True)
    def __str__(self):
        return self.title