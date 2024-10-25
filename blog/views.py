from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'title' : 'blog 1',
        'post_date' : '12-45-75',
        'content' : 'this is my first blog'
    },
        {
        'title' : 'blog 2',
        'post_date' : '55412-75',
        'content' : 'this is my second blog'
    }
]

# Create your views here.

def home(request):
    context = { 
        'posts' :posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html' , {'title' : 'about'})
