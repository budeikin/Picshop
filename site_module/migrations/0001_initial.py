# Generated by Django 4.0.4 on 2022-04-29 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=200)),
                ('site_url', models.CharField(max_length=200, verbose_name='Domain Name')),
                ('site_logo', models.ImageField(upload_to='images/site-setting/')),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('copy_right', models.TextField()),
                ('about_us_text', models.TextField()),
                ('is_main_setting', models.BooleanField()),
            ],
        ),
    ]