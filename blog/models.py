from django.db import models

class Article(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок статьи",
        help_text="Введите заголовок статьи"
    )
    description = models.TextField(
        verbose_name="Содержимое статьи",
        help_text="Введите содержимое статьи",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="photos/",
        verbose_name="Превью(изображение)",
        help_text="Загрузите изображение",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания статьи",
        help_text="Введите дату создания статьи",
    )
    is_published = models.BooleanField(
        verbose_name='Признак публикации',
        default=False,
        help_text='Отметьте для публикации статьи',
    )
    views_count = models.PositiveIntegerField(
        verbose_name='Количество просмотров',
        default=0,
        help_text='Укажите количество просмотров',
        blank=True
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["title"]
