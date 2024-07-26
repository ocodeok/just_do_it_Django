from django.db import models


class News(models.Model):
    title = models.CharField(max_length=120, verbose_name="Название новости")
    content = models.TextField(blank=True, verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    updated_at = models.DateTimeField(auto_now=True , verbose_name="Фото")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Фото", blank=True)
    is_published = models.BooleanField(default=False, verbose_name="Опубликованно")

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at', 'title']
