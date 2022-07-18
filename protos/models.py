from django.db import models
from annotations import Annotations
from selections import Selections

# Create your models here.

class TestUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()


