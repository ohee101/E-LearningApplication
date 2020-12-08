from django import forms
from App_Courses.models import Questions, Replies

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['question']

class ReplyForm(forms.ModelForm):
    class Meta: 
        model = Replies
        fields = ['reply']