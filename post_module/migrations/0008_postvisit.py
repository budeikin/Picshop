# Generated by Django 4.0.4 on 2022-05-15 02:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post_module', '0007_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30, verbose_name='user ip')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_module.post', verbose_name='post')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post Visit',
                'verbose_name_plural': 'Post Visits',
            },
        ),
    ]
