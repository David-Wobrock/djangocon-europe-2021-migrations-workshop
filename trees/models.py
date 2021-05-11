from django.db import models


class Tree(models.Model):
    name = models.CharField(max_length=25)
