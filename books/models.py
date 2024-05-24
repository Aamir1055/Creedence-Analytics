from djongo import models

class Book(models.Model):
    name = models.CharField(max_length=255,default='null')
    img = models.URLField(default='null')
    summary = models.TextField(default='null')

    def __str__(self):
        return self.name
