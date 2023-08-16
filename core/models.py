from django.db import models
from django.contrib.auth.models import User

class InputValue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    input_values = models.TextField()

    def __str__(self):
        return str(f"{self.id} - {self.user.id}")