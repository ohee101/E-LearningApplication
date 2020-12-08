from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='instructor_profile')
    first_name = models.CharField(max_length=264, blank=True)
    last_name = models.CharField(max_length=264, blank=True)
    email = models.EmailField(blank=True)
    job_position = models.CharField(max_length=264, blank=True)
    subject = models.CharField(max_length=264, blank=True)

    def __str__(self):
        return self.user.username

class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='learner_profile')
    first_name = models.CharField(max_length=264, blank=True)
    last_name = models.CharField(max_length=264, blank=True)
    email = models.EmailField(blank=True)
    institution = models.CharField(max_length=264, blank=True)

    def __str__(self):
        return self.user.username
    