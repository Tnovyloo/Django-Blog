from django.urls import path
# from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    # path('', views.index, name='')
    path('', HomeView.as_view(), name='index'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('update_post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('delete_post/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
]
