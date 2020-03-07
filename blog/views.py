from django.shortcuts import render
from .models import Post

 # from django.http import HttpResponse not needed at the moment
# Create your views here.



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    # Old way, returns HTML in the parenthesis return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})
