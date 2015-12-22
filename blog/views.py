from django.shortcuts import render
from django.utils import timezone
from .models import Posts

def index(request):
    posts = Posts.objects.filter(created__lte = timezone.now()).order_by('-created')
    return render(request, 'blog/index.html', {'posts':posts})
