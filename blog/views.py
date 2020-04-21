from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from users.models import Profile

"""
There are a lot of class based view types, with a lot of functionality.
Our home page is a good fit for a class list view, because it lists the
posts being shown.
"""


# This is the less fancy function view, in order to view the homepage
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


# class view to see all of the posts on the home page (also paginated)
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # Orders our post from newest to oldest
    paginate_by = 10


# class view to see the specific posts of a user, also includes the user's bio, which is why two views are imported
class UserPostListView(ListView):
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs.get('username'))

        context = super(UserPostListView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.filter(author=user).order_by('-date_posted')
        context['Profile'] = Profile.objects.get(user=user)
        return context

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

# This mixin means we can only make a post while logged in, and we will be
# redirected to log-in if the user isn't
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def LikePost(request, pk):
    model_to_like = Post.objects.get(id=pk)
    print(model_to_like)
    model_to_like.likes += 1
    model_to_like.save()
    returned_link = '/post/' + str(pk) + '/'
    return HttpResponseRedirect(returned_link)

def contact(request):
    return render(request, "blog/contact.html")

def about(request):
    # Old way, returns HTML in the parenthesis return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})
