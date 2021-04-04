from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    subtitle = models.CharField(max_length=200, blank=True)
    # image = models.ImageField(upload_to='blog/images/', blank=True)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.title

