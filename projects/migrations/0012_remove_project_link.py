# Generated by Django 3.0.7 on 2020-09-18 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_project_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='link',
        ),
    ]
