from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, UpdatePostForm, AddCategoryForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['post_date']
    cats = Category.objects.all()

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        # context = {"category_menu": category_menu}
        context["category_menu"] = category_menu
        return context

def CategoryView(request, category):
    category_posts = Post.objects.filter(category=category.replace('-', ''))
    return render(request, 'categories.html', {'category_posts': category_posts,
                                               'category': category.replace('-', ' ')})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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
