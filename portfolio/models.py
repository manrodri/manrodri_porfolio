from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    # points to where images are. MEDIA IS THE ROOT FOR THIS.
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True) # can be null

    def __str__(self):
        return self.title
