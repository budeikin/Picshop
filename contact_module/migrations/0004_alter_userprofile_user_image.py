# Generated by Django 4.0.4 on 2022-04-26 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0003_rename_image_userprofile_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
