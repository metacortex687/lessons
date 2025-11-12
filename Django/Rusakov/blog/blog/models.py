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

    preview = models.CharField(
        validators=[MinLengthValidator(5)],
        max_length=300,
        verbose_name="Превью",
        help_text="Отображается в списке статей",
    )
    content = models.TextField(verbose_name="Текст статьи")

    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Автор")

    photo = models.ImageField(upload_to="images", verbose_name="Изображения")

    date = models.TimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]
        verbose_name = "Статья"
        vebose_name_plural = "Статьи"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField(
        max_length=70, validators=[MinLengthValidator(1)], verbose_name="Имя"
    )
    email = models.EmailField()

    content = models.TextField()
    date = models.TimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]
        verbose_name = "Комментарий"
        vebose_name_plural = "Комментарии"


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
        vebose_name_plural = "Обратная связь"
