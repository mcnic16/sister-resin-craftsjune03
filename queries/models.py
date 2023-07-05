from django.db import models


class Query(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name'] 
 
    def __str__(self):
        return f"Form by {self.name}"


