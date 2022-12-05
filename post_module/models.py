from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from account_module.models import User


# Create your models here.
class Profession(models.Model):
    title = models.CharField(max_length=100)
    title_url = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    # profile = models.ImageField()
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, null=True, related_name='persons')
    description = models.TextField(db_index=True, null=True)
    image = models.ImageField(upload_to='images/persons', null=True, blank=True)
    email = models.EmailField(null=True)

    def get_absolute_url(self):
        return reverse('detail_of_persons', args=[self.id])

    # def save(self,*args,**kwargs):
    #     self.slug = slugify(self.name)
    #     super().save(*args,**kwargs)

    def __str__(self):
        return f'{self.name}({self.profession})'


# class PostVisit(models.Model):
#     post = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name='post')
#     ip = models.CharField(max_length=30, verbose_name='user ip')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#
#     def __str__(self):
#         return f"{self.post.name} / {self.ip}"
#
#     class Meta:
#         verbose_name = 'Post Visit'
#         verbose_name_plural = 'Post Visits'
