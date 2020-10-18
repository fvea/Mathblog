""" Defines URL patterns for blog_QA """

from django.urls import path

from . import views

app_name = 'blog_QA'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]