from django.db import models

class User(models.Model):
    first_name = models.CharField(255)
    last_name = models.CharField(255)
    email_address = models.CharField(255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
