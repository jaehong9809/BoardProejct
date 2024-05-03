from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=200, blank=True, null=True)
    likenum = models.IntegerField(null=True)

    class Meta:
        managed = False
        db_table = 'article'
