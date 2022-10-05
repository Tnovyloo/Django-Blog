from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment, Profile, User
from .forms import PostForm, UpdatePostForm, AddCategoryForm, AddCommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['post_date']
    cats = Category.objects.all()

    # def get_context_data(self, *args, **kwargs):
    #     category_menu = Category.objects.all()
    #     context = super(HomeView, self).get_context_data(*args, **kwargs)
    #     # context = {"category_menu": category_menu}
    #     context["category_menu"] = category_menu
    #     return context

class SearchView(ListView):
    model = Post
    template_name = 'search_user.html'
    cats = Category.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            data = User.objects.filter(username=search)
        return data

def category_view(request, category):
    category_posts = Post.objects.filter(category=category.replace('-', ''))
    return render(request, 'categories.html', {'category_posts': category_posts,
                                               'category': category.replace('-', ' ')})

def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST['post_id'])
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        post_object = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post_object.total_likes()
        liked = False
        if post_object.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked

        return context


class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'add_post_comment.html'

    def get_success_url(self):
        article_id = self.kwargs['pk']
        # return reverse_lazy('article', kwargs={'pk': article_id}) # return to article.
        return reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)


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
