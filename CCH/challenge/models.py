from django.db import models
from django.contrib.auth.models import User

from challenge.utils import generate_file_name


# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='Questions')
    name = models.CharField(max_length=255, null=True)
    file = models.FileField(upload_to=generate_file_name)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -> {self.name}"

    @property
    def get_user_questions(self):
        return 