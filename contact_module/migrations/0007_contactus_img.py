# Generated by Django 4.0.4 on 2022-05-07 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0006_remove_contactus_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='img',
            field=models.ImageField(null=True, upload_to='images/contact'),
        ),
    ]