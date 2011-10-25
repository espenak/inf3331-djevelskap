from django.db import models

# Create your models here.
class Delivery(models.Model):
    assignment = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    contents = models.TextField()
    feedback = models.TextField()

    class Meta:
        unique_together = ('assignment', 'user')
