# Generated by Django 4.0.4 on 2022-05-07 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0007_contactus_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='img',
        ),
    ]
