from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, UpdatePostForm, AddCategoryForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    # ordering = ['-id']
    ordering = ['post_date']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__' #we dont have to use it when we did a form
    # # fields = ('title', 'body', 'title_tag')

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    form_class = AddCategoryForm

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = UpdatePostForm
    # fields = ['title', 'title_tag', 'body'] #we dont have to use it when we did a form

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')
