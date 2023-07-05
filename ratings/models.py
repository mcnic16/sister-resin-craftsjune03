from django.db import models
from products.models import Product
from profiles.models import UserProfile


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars = models.IntegerField(default=0)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating for {self.product} by {self.comment}"
