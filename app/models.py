from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    author = models.CharField(max_length=100, verbose_name="Автор")
    published_date = models.DateField(verbose_name="Дата публикации")
    isbn = models.CharField(max_length=20, verbose_name="ISBN")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
