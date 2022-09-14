from django.db import models


class Cats(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Moto(models.Model):
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")
    is_published = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    cats = models.ForeignKey(Cats, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мотоцикл"
        verbose_name_plural = "Мотоциклы"
