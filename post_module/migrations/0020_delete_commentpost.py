# Generated by Django 4.0.4 on 2022-11-12 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_module', '0019_alter_commentpost_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CommentPost',
        ),
    ]
