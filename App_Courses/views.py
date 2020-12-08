from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy


from django.utils.text import slugify
from App_Login.models import Instructor, Learner
from App_Courses.models import Courses, Questions, Replies
from App_Courses.forms import QuestionForm, ReplyForm

import uuid

# Create your views here.

class Home(ListView):
    context_object_name = 'course_list'
    model = Courses
    template_name = 'App_Courses/home.html'

class PublishCourse(LoginRequiredMixin, CreateView):
    model = Courses
    template_name = 'App_Courses/publish_course.html'
    fields = ('course_title', 'course_front', 'course_article')

    def form_valid(self, form):
        course_object = form.save(commit=False)
        course_object.instructor = self.request.user.instructor_profile
        title = course_object.course_title
        course_object.slug = slugify(title.replace(" ", "-") + str(uuid.uuid4()))
        course_object.save()
        return HttpResponseRedirect(reverse('App_Courses:home'))

@login_required
def course_description(request, slug):
    course = Courses.objects.get(slug=slug)
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user.learner_profile
            question.course = course
            question.save()
            return HttpResponseRedirect(reverse('App_Courses:course_description', kwargs={'slug': slug}))

    return render(request, 'App_Courses/course_description.html', context={'course': course, 'form': form})

class MyCourses(LoginRequiredMixin, TemplateView):
    template_name = 'App_Courses/my_courses.html'

@login_required
def question(request, pk):
    form = ReplyForm()
    question = Questions.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.question = question
            reply.save()
            return HttpResponseRedirect(reverse('App_Courses:question', kwargs={'pk': pk}))
    return render(request, 'App_Courses/question.html', {'form':form, 'question': question})
