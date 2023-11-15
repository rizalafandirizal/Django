from django.db import models

class Data_diri(models.Model):
  Name = models.CharField(max_length=255)
  Email = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.Name}"