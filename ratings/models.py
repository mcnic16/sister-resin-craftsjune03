from django.db import models
from django.contrib.auth.models import User

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(default=0)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.stars} stars'

    class Meta:
        ordering = ['-created_at']


class Product(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

