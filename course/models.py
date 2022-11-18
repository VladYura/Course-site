from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.SET_NULL, null=True)
    data = models.CharField('Комбинация', max_length=50)

    def __str__(self):
        return f'{self.user} - {self.data}'

    class Meta:
        verbose_name = 'Данные пользователя'
        verbose_name_plural = 'Данные пользователя'
