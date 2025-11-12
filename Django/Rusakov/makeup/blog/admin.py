from django.contrib import admin

# Register your models here.
from blog.models import Article, Comment, Feedback, Image

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Feedback)
admin.site.register(Image)
