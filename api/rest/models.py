from django.contrib.auth.models import User
from django.db import models


class Ticket(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_decided = models.BooleanField(default=False)
    is_not_decided = models.BooleanField(default=True)
    is_freeze = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    content = models.TextField(blank=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True, related_name='tickets')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,  blank=True, null=True, related_name='children')

    def __str__(self):
        return f"{self.content}"
