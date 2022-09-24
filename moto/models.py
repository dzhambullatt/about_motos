from django.db import models
from django.urls import reverse


class Cats(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название", db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Moto(models.Model):
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время Создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    cats = models.ForeignKey(Cats, on_delete=models.CASCADE, verbose_name="Категория")

    def get_absolute_url(self):
        return reverse('view_moto', kwargs={'moto_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мотоцикл"
        verbose_name_plural = "Мотоциклы"


