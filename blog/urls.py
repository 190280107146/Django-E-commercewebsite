from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="indexBlog"),
    path("blogpost/<int:id>", views.blogpost, name="blogPost")
]
