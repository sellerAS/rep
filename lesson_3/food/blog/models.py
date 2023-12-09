from django.db import models


class Autor(models.Model):
    username = models.CharField(max_length=20, verbose_name='LOGIN')
    firstname = models.CharField(max_length=20, verbose_name='FIO')
    lastname = models.CharField(max_length=20, verbose_name='FAMILYA')
    email = models.EmailField(verbose_name='EMAIL', max_length=50)

    class Meta:
        db_table = 'autors'

    def __str__(self):
        return f'{self.username}'

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=20, verbose_name='Заголовок', db_index=True)
    content = models.TextField(verbose_name='Содержание', default='')
    published_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True)
    status_choices = [
        ('a', 'Active'),
        ('i', 'Inactive')
    ]
    activity_flag = models.CharField(max_length=1, choices=status_choices, default='i')
    # autor = models.ForeignKey(Autor, verbose_name='автор', on_delete=models.CASCADE)

    class Meta:
        db_table = 'news'
        ordering = ['-published_at']
        permissions = [
            ('can_publish', 'Может опубликовать новость')
        ]

    def __str__(self):
        return f'{self.title}'





