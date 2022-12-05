from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/avatars',null=True,blank=True)
    email_active_code = models.CharField(max_length=100)
    about_user = models.TextField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        return self.email
