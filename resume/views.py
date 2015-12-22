from django.shortcuts import render
from django.utils import timezone


def resume(request):
    return render(request, 'resume/resume.html',)
