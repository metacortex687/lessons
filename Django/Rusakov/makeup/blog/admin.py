from django.contrib import admin

# Register your models here.
from blog.models import Article, Comment, Feedback, Image

admin.site.register(Article)
admin.site.register(Feedback)
admin.site.register(Image)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("date", "author", "article", "content")

    search_fields = ('author',)

    date_hierarchy = "date"
