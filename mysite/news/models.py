from django.db import models


class News(models.Model):
    title = models.CharField(max_length=120, verbose_name="Название новости")
    content = models.TextField(blank=True, verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Фото")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Фото", blank=True)
    is_published = models.BooleanField(default=False, verbose_name="Опубликованно")
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True, verbose_name="Категория")

    def __str__(self):
        return f"Новость: {self.title}"

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at', 'title']


class Category(models.Model):
    title = models.CharField(max_length=125, db_index=True, verbose_name="Наименование категории")

    def __str__(self):
        return f"Категория {self.title}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title']
