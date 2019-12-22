from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50, default="Project Name")
    url = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="images/projects/")
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.name
