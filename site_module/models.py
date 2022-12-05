from django.db import models

# Create your models here.
class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200)
    site_url = models.CharField(max_length=200,verbose_name='Domain Name')
    site_logo = models.ImageField(upload_to='images/site-setting/')
    email = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=200,null=True,blank=True)
    copy_right = models.TextField()
    about_us_text = models.TextField()
    is_main_setting = models.BooleanField()
    def __str__(self):
        return self.site_name
