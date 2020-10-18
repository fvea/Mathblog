from django.shortcuts import render

# Create your views here.

def index(request):
    """ The home page for the MathBlog. """
    return render(request, 'blog_QA/index.html')
