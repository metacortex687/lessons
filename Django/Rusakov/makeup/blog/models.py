from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator


# class Author(
#     models.Model
# ):  # пользователя не хочу использовать, так как не все пользователи авторы. Автором становишься после написания статьи. Или иных предусловий.
#     nick_name = models.CharField(max_length=50)  # не уверен насколько нужно
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор"
#     )

#     class Meta:
#         verbose_name = "Автор"
#         verbose_name_plural = "Авторы"


class Image(models.Model):
    description = models.CharField(
        validators=[MinLengthValidator(1)],
        max_length=150,
        verbose_name="Описание",
        help_text="Введите описание",
        blank=True,
        default="",
    )
    date = models.TimeField(auto_now_add=True)

    file = models.ImageField(upload_to="images", verbose_name="Изображения")

    def __str__(self):
        return self.file.name.split("/")[1]


class Article(models.Model):

    title = models.CharField(
        validators=[MinLengthValidator(2)],
        max_length=70,
        verbose_name="Заголовок",
        help_text="Введите название статьи",
    )

    subtitle = models.CharField(
        max_length=255, verbose_name="Подзаголовок", blank=True, default=""
    )

    @property
    def preview(self):
        return (self.content[:300] + "...") if len(self.content) > 300 else self.content

    # preview = models.CharField(
    #     validators=[MinLengthValidator(5)],
    #     max_length=300,
    #     verbose_name="Превью",
    #     help_text="Отображается в списке статей",
    # )
    content = models.TextField(verbose_name="Текст статьи")

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="Автор", on_delete=models.RESTRICT
    )

    image = models.ForeignKey(
        Image, on_delete=models.SET_NULL, null=True, verbose_name="Заглавная картинка"
    )

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} {self.title}"

    class Meta:
        ordering = ["-date"]
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField(
        max_length=70, validators=[MinLengthValidator(1)], verbose_name="Имя"
    )
    email = models.EmailField(null=True, blank=True)

    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.article.id} {self.author} {self.date.date()}: {self.content[0:20]} -> {self.article.title}"

    class Meta:
        ordering = ["-date"]
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Feedback(models.Model):
    author = models.CharField(
        max_length=70, validators=[MinLengthValidator(1)], verbose_name="Имя"
    )
    email = models.EmailField()
    content = models.TextField()
    date = models.TimeField(auto_now_add=True)

    STATUSES = [("NEW", "Новая обартная связь"), ("PCD", "Обработано")]

    status_feed_back = models.CharField(
        choices=STATUSES, max_length=3, verbose_name="Статус"
    )

    class Meta:
        ordering = ["-date"]
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"
