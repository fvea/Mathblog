from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm

# Create your views here.

def index(request):
    """ The home page for the MathBlog. """
    return render(request, 'blog_QA/index.html')

def topics(request):
    """ Show all topics. """
    topics = Topic.objects.order_by('-date_added')
    context = {'topics': topics}
    return render(request, 'blog_QA/topics.html', context)

def topic(request, topic_id):
    """ Show a single topic and its entries. """
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'blog_QA/topic.html', context)

def new_topic(request):
    """ Add a new topic. """
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_QA:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blog_QA/new_topic.html', context)


