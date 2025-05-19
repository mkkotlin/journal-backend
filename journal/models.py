from django.db import models
from  django.contrib.auth.models import User
# Create your models here.

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add = True)
    title = models.CharField(max_length=200)
    mood = models.CharField(max_length = 20)
    is_private = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.title}({self.user.username})"


class JournalEntry(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='jornal_entries')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title