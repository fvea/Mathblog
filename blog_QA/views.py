from django.shortcuts import render

from . models import Topic

# Create your views here.

def index(request):
    """ The home page for the MathBlog. """
    return render(request, 'blog_QA/index.html')

def topics(request):
    """ Show all topics. """
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'blog_QA/topics.html', context)




