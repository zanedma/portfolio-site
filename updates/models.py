from django.db import models

class Update(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def summary(self):
        if len(self.body) <= 100:
            return self.body
        else:
            return self.body[:100] + '...'
