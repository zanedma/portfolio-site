# Generated by Django 3.0.7 on 2020-06-17 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200617_0033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='technology',
        ),
        migrations.AddField(
            model_name='project',
            name='body',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
