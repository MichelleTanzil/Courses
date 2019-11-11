from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *


def index(request):
    context = {
        'all_courses': Course.objects.all()
    }
    return render(request, 'main_app/index.html', context)


def add_course(request):
    errors = Course.objects.basic_validator(request.POST)
    errors_desc = Description.objects.basic_validator(request.POST)
    if len(errors) > 0 or len(errors_desc) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        for key, value in errors_desc.items():
            messages.error(request, value)
        return redirect('/')
    else:
        description1 = Description.objects.create(
            content=request.POST['description'])
        Course.objects.create(
            name=request.POST['name'], description=description1)
        messages.success(request, "Course successfully added")
        return redirect('/')


def course_profile(request, course_id):
    context = {
        'course_in_question': Course.objects.get(id=course_id)
    }
    return render(request, 'main_app/course_profile.html', context)


def DNDestroy(request):
    return redirect('/')


def destroy_course(request, course_id):
    course_in_question = Course.objects.get(id=course_id)
    course_in_question.delete()
    return redirect('/')

def comments_profile(request, course_id):
    course = Course.objects.get(id=course_id)
    context = {
        'course': course,
        'course_comments': Comment.objects.filter(course=course)
    }
    return render (request, 'main_app/comments_profile.html', context)

def add_comment(request,course_id):
    course = Course.objects.get(id=course_id)
    Comment.objects.create(content=request.POST['comment'], course=course)
    return redirect(f'/comments_profile/{course_id}')