# Generated by Django 3.0.7 on 2020-09-18 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20200918_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, default=''),
        ),
    ]
