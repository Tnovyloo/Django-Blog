from django.contrib import admin
from .models import Post, Category, Profile, Comment
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Comment)

# If you want you could connect profile with user.
#
# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'profile'
#
# class UserAdmin(BaseUserAdmin):
#     inlines = [ProfileInline]
#
#
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
