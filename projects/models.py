from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True)
    featured = models.BooleanField(default=False)
    summary = models.TextField(max_length=200)
    body = models.TextField()
    link = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.name
