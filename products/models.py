from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="media/", verbose_name='Фото')
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Review(models.Model):
    text = models.CharField(max_length=300, verbose_name="Текст отзыва")
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
