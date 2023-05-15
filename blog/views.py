from django.shortcuts import render
from .models import Post

# Create your views here.

posts = [
    {
        'author':'Mary',
        'title':'Blog Post 1',
        'content' : 'First post content',
        'data_posted' : 'August 27, 2021'
    },
    {
        'author':'Jane',
        'title':'Blog Post 2',
        'content' : 'Second post content',
        'data_posted' : 'August 28, 2021'
    },
]

def home(request):
    content = {
        'title':'Home-Page',
        'posts': Post.objects.all(),
        'name':'Mary',
        
        }
    return render(request, 'blog/home.html', content)

def about(request):
    content = {
        'title':'Home-Page',
        'posts':posts,
        'name':'Mary',
        
        }
    return render(request, 'blog/about.html', content)