from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model

# Create your models here.
class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title