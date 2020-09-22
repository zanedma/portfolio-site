from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class Home(models.Model):
    header = models.CharField(max_length=100)
    welcome_msg = models.TextField()
    headshot = models.ImageField(upload_to='images/', blank=True)

    def save(self, *args, **kwargs):
        if not self.pk and Home.objects.exists():
            raise ValidationError('Only one Home instance allowed')
        return super(Home, self).save(*args, **kwargs)
