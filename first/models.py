from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from stdimage import StdImageField, JPEGField
from django.urls import reverse
#from django.core.validators import RegexValidator
#from phone_field import PhoneField
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    tokuten = models.CharField(max_length=80)
    content = models.TextField()
    name = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    #img = models.ImageField(upload_to='img/',null=True)
    tell = models.CharField( max_length=15, blank=True)
    email = models.EmailField(null=True,blank=True)
    url = models.URLField(null=True,blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    img = StdImageField(upload_to='path/to/img', blank=True, variations={
        'large': (600, 257.14),
        'thumbnail': (360, 234.7, True),
        'medium': (300, 300),
        })

  
    def updated(self):
        self.updated = timezone.now()
        return save()

    def __str__(self):
        return str(self.name) + ':'  + self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


class LinePush(models.Model):

    user_id = models.CharField('ユーザーID',max_length=100,unique=True)

    def __str__(self):
        return self.user_id