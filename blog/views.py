from django.shortcuts import render, get_object_or_404

from .models import Post
from django.contrib.auth.models import User 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView, 
    DetailView
)
# Create your views here.

from blog.forms import PostForm

class HomeView(ListView):
    model = Post
    queryset = Post.objects.all()
    context_object_name ='posts'
    ordering = ['-created']
    paginate_by = 15
    template_name = 'homeview.html'
    
    
    
class CreatorsPosts(ListView):
    model = Post 
    template_name = 'creatorsposts.html'
    paginate_by = 15 
    context_object_name = 'posts'
    
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(creator=user).order_by('-created')
    
    
    
class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.all()
    context_object_name ='posts'
    ordering = ['-created']
    paginate_by = 15
    template_name = 'postsdetailview.html'
    
    
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    queryset = Post.objects.all()
    context_object_name ='posts'
    template_name = 'postscreateview.html'
    form_class = PostForm
    success_url = ''
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
    
    
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'postsupdateview.html'
    model  = Post 
    form_class = PostForm
    
    
    def form_valid(self, form):
        form.instance.creator = self.request.user 
        return super().form_valid(form)
    
    def test_func(self):
        post_to_be_updated = self.get_object()
        if self.request.user == post_to_be_updated.creator :
            return True
        return False
    
    
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'postdeleteview.html'
    context_object_name ='post'


    def test_func(self):
        post_to_be_deleted = self.get_object()
        if self.request.user == post_to_be_deleted.creator:
            return True
        return False