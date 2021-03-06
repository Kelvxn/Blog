from django.contrib import admin

from .models import BlogPost, Comment


# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date_added")
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}
    inlines = [CommentInline]


admin.site.register(Comment)
