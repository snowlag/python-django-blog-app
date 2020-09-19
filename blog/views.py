from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
from .models import Article
from blog.forms import BlogForm 
from blog.forms import  ArticleForm, LoginForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url = "/login/")
def index(request):
    return HttpResponse("hello World from ankit")


@login_required(login_url = "/login/")
def get_blogs(request): 
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request , 'blog/blogs.html' , context)


@login_required(login_url = "/login/")
def add_blog(request , blog_id = None):
    if blog_id:
        blog = Blog.objects.get(id=blog_id)
    else:
        blog= Blog()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return get_blogs(request)
        else:
            context = {'form' : form}
            return render(request , "add_blog.html" , context)
    blog_form = BlogForm(instance = blog)
    context = {'form': blog_form , 'blog': blog}
    return render(request , 'add_blog.html' , context)