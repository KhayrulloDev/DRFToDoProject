from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class ToDo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    memo = models.TextField(verbose_name='Memo')
    important = models.BooleanField(default=False, verbose_name='Important')
    completed = models.BooleanField(default=False, verbose_name='Completed')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return f"{self.title}"

