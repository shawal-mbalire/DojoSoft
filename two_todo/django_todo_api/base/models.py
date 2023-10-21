from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL # auth.User

class Todo(models.Model):
    user        = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title       = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField(blank=True, null=True)
    completed   = models.BooleanField(default=False)

