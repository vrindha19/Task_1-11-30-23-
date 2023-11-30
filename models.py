from django.db import models

class RegisterModel(models.Model):
    name=models.CharField(max_length=256)
    email=models.EmailField()
    Password=models.TextField( )

    def __str__(self) -> str:
        return self.name
