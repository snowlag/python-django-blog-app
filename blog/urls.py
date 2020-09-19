from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('index/' , views.index , name = 'index'),
    path('get_blogs/' , views.get_blogs , name = 'get_blogs'),
    path('add_blog/' , views.add_blog , name = "Add Blog"),
    path('add_blog/<int:blog_id>' , views.add_blog , name='edit_blog'),

]