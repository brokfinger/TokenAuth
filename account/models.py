from django.db import models
from django.contrib.auth.models import User


class UserEntranceCount(models.Model):
    """
    Модель для сохранения количества входа пользователя по ссылке.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField(default=0, blank=True)
