from django.db import models

from core.models import User


class TgUser(models.Model):
    chat_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=100, null=True, blank=True, default=None)
    user = models.ForeignKey(User, on_delete=models.PROTECT,null=True,blank=True,default=None)

    def __str__(self):
        if self.username:
            return self.username
        elif self.user and self.user.username:
            return self.user.username
        else:
            return super().__str__()


    class Meta:
        verbose_name = "tg пользователь"
        verbose_name_plural = "tg пользователи"

