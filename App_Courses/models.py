from django.db import models
from django.contrib.auth.models import User
from App_Login.models import Instructor, Learner
from django.utils.text import slugify
import uuid

# Create your models here.

class Courses(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='course_instructor')
    course_title = models.CharField(max_length=264)
    course_front = models.ImageField(verbose_name='Add a course front', upload_to='course_fronts')
    course_article = models.TextField(verbose_name='Course Article')
    slug = models.SlugField(max_length=264, unique=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_title

    def save(self):
        self.slug = slugify(self.course_title + '-' + str(uuid.uuid4()))
        super(Courses, self).save()


class Questions(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='course_question')
    user = models.ForeignKey(Learner, on_delete=models.CASCADE, related_name='learner_question')
    question = models.TextField()
    question_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-question_time']

    def __str__(self):
        return self.question
    
class Replies(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='question_reply')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reply')
    reply = models.TextField()
    reply_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reply
    