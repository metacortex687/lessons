from django.db import models
from django.conf import settings


class Author(
    models.Model
):  # пользователя не хочу использовать, так как не все пользователи авторы. Автором становишься после написания статьи. Или иных предусловий.
    nick_name = models.CharField(max_length=50)  # не уверен насколько нужно
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Photo(models.Model):
    describe = models.CharField(max_length=150)
    path = models.CharField(
        max_length=150
    )  # в иидеале должно генерироваться возможно UUIDField и под ним сохранять
    author = models.OneToOneField(
        "Author", on_delete=models.CASCADE
    )  # Решил явно указать кто грузит. Что бы только свои картинки могли использовать

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


class Article(models.Model):
    title = models.CharField(
        max_length=70,
        help_text="Введите название статьи",
        verbose_name="Название статьи",
    )
    authors = models.ManyToManyField(
        Author, through="ArticleAuthor", through_fields=("article", "author")
    )

    photos = models.ManyToManyField(
        Photo, through="ArticlePhoto", through_fields=("article", "photo")
    )

    content = models.TextField()
    date = models.TimeField()


class ArticlePhoto(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)


class ArticleAuthor(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
