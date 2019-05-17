from django.db import models


class Subscriber(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('-created_at', )
