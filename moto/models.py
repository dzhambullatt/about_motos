from django.db import models


class Cats(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")


class Moto(models.Model):
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")
    is_published = models.BooleanField(blank=True)
    time_create = models.DateTimeField()
    time_update = models.DateTimeField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    cats = models.ForeignKey(Cats, on_delete=models.CASCADE)


