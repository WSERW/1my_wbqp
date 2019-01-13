from django.db import models

class Question(models.Model):
    level = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    ask = models.TextField()
    answer1 = models.CharField(max_length=30)
    answer2 = models.CharField(max_length=30)
    answer3 = models.CharField(max_length=30)
