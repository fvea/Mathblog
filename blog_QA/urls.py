""" Defines URL patterns for blog_QA """

from django.urls import path

from . import views

app_name = 'blog_QA'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Page for adding a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry.
    path('entries/<int:topic_id>/', views.entries, name='entries'),
    # Page for editing a topic.
    path('edit_topic/<int:topic_id>/', views.edit_topic, name='edit_topic'),
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]