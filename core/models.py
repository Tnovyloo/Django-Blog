from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=255, default="Nothing's there")
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile",
                                    default='user-profile-icon.jpg')
    # Social links
    social_link1 = models.CharField(max_length=255, null=True, blank=True, default="Awesome profile link 1!")
    social_link2 = models.CharField(max_length=255, null=True, blank=True, default="Awesome profile link 2!")
    social_link3 = models.CharField(max_length=255, null=True, blank=True, default="Awesome profile link 3!")

    def __str__(self):
        return str(self.user)

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('index')

    class Meta:
        verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/headers")
    title_tag = models.CharField(max_length=255, default="Bloog!")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='unknown')
    snippet = models.CharField(max_length=255, default='Click link above to read blog post')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('index')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post)
