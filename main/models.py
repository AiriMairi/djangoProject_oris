from django.db import models


# Create your models here.

class Order(models.Model):
    name = models.CharField(
        max_length=159,
        verbose_name='название',
    )
    importance = models.CharField(
        max_length=12,
        verbose_name='очень срочно/срочно/не срочно '
    )
    date = models.DateTimeField(
        verbose_name='дата и время',
    )
    count = models.IntegerField(
        verbose_name='Номер',
        default=1,
    )

    def __str__(self):
        return f'{self.importance}---{self.name}'
