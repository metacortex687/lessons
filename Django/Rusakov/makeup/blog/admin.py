from django.contrib import admin

# Register your models here.
from blog.models import Article, Comment, Feedback, Image


admin.site.register(Image)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("date", "author", "article", "content")

    search_fields = ("author",)

    date_hierarchy = "date"


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_filter = ("status_feed_back",)
    list_display = ("date", "author", "title")


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "author", "title")
    
    date_hierarchy = "date"
