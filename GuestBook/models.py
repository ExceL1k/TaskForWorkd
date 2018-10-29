from django.db import models

# Create your models here.


class BookGuest(models.Model):
    name = models.CharField(max_length=60, null=False)
    email = models.EmailField(max_length=60, null=False)
    link = models.URLField(max_length=60, null=True, blank=True)
    textMessage = models.TextField(max_length=250, null=True)
    ip = models.CharField(max_length=60, null=True)
    cashBrowser = models.CharField(max_length=60, null=True)
    img = models.ImageField(upload_to='image', blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
