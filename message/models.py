from django.db import models

# Create your models here.

class Message(models.Model):
  text = models.CharField(max_length = 500)
  pub_date = models.DateTimeField("date published")