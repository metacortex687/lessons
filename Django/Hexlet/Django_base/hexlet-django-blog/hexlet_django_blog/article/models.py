from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ArticleComment(models.Model):
    #article = models.ForeignKey(Article)
    content = models.CharField('content', max_length=100)