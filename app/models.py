import datetime
from django.db import models

class Book(models.Model):
    class Ganre(models.TextChoices):
        FICTION = 'FI', 'Художественная литература'
        NONFICTION = 'NF', 'Документальная литература'
        FANTASY = 'FA', 'Фантастика'
        SCIFI = 'SF', 'Научная фантастика'
        MYSTERY = 'MY', 'Детектив'
        ROMANCE = 'RO', 'Романтика'
        THRILLER = 'TH', 'Триллер'
        HORROR = 'HO', 'Ужасы'
        HISTORICAL = 'HI', 'Историческая литература'
        BIOGRAPHY = 'BI', 'Биография'
        POETRY = 'PO', 'Поэзия'
        DRAMA = 'DR', 'Драма'
        COMIC = 'CO', 'Комикс'
        CLASSIC = 'CL', 'Классическая литература'
        CHILDREN = 'CH', 'Детская литература'
        ADVENTURE = 'AD', 'Приключения'
        FABLE = 'FB', 'Басня'
        MYTHOLOGY = 'MYT', 'Мифология'
        ESSAY = 'ES', 'Эссе'
        SCIENCE = 'SCI', 'Научная литература'

    title = models.CharField(max_length=100 , verbose_name='название')
    description = models.CharField(max_length=255 , verbose_name='описание')
    author = models.CharField(max_length=100 , verbose_name='автор')
    published_year = models.DateField(verbose_name='дата публикации')
    price = models.IntegerField(verbose_name='цена')
    created_at = models.DateTimeField(auto_now=True , verbose_name='созданно')
    updated_at = models.DateTimeField(auto_now_add=True , verbose_name='обновленно')
    genre = models.CharField(max_length=100, choices=Ganre, verbose_name='жанр')

    def __str__(self):
        return f'{self.title} ({self.author}) - {self.published_year}'

    class Meta:
        verbose_name = 'Книги'

    
    