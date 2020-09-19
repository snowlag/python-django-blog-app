from blog.models import Blog , Article
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class BlogForm (forms.ModelForm):
    class Meta:
        model = Blog
        fields  = ['name']
        
class ArticleForm( forms.ModelForm):
    class Meta:
        model = Article
        fields  = ['title' , 'body' , 'draft']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label = "Username" , max_length = 30 , widget = forms.TextInput(attrs = {'name': 'username'}))
    password = forms.Charfield( label = "Password" , max_length = 30 , widget = forms.PasswordInput(attrs = {'name': 'password'}))
