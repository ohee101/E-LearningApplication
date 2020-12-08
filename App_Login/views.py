from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from App_Login.models import Instructor, Learner
from App_Login.forms import LoginForm, SignUpForm, InstructorForm, LearnerForm

# Create your views here.

def homepage(request):
    return render(request, 'App_Login/homepage.html', context={})


def instructor_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Login:instructor_profile'))
    return render(request, 'App_Login/login.html', context={'instructor':True, 'form':form})

def learner_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Login:learner_profile'))
    return render(request, 'App_Login/login.html', context={'form':form})


def instructor_signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            instructor_profile = Instructor(user=request.user)
            instructor_profile.save()
            return HttpResponseRedirect(reverse('App_Login:instructor_login'))
    return render(request, 'App_Login/signup.html', context={'instructor': True, 'form':form}) 

def learner_signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            learner_profile = Learner(user=request.user)
            learner_profile.save()
            return HttpResponseRedirect(reverse('App_Login:learner_login'))
    return render(request, 'App_Login/signup.html', context={'form':form}) 


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:homepage'))


@login_required
def instructor_profile(request):
    return render(request, 'App_Login/profile.html', context={'instructor': True})

@login_required
def learner_profile(request):
    return render(request, 'App_Login/profile.html', context={})



@login_required
def edit_instructor(request):
    current_user = Instructor.objects.get(user=request.user)
    form = InstructorForm(instance=current_user)
    if request.method == 'POST':
        form = InstructorForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = InstructorForm(instance=current_user)
            return HttpResponseRedirect(reverse('App_Login:instructor_profile'))
    return render(request, 'App_Login/edit_profile.html', context={'form': form})

@login_required
def edit_learner(request):
    current_user = Learner.objects.get(user=request.user)
    form = LearnerForm(instance=current_user)
    if request.method == 'POST':
        form = LearnerForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = LearnerForm(instance=current_user)
            return HttpResponseRedirect(reverse('App_Login:learner_profile'))
    return render(request, 'App_Login/edit_profile.html', context={'form': form})
 