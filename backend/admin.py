from django.contrib import admin
from .models import Post, Project, Feedback, ContactRequest


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'date_created']
    search_fields = ['title', 'content']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    pass
