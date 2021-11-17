from django.db import models

class SinglePost(models.Model):
    tag= models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    content= models.TextField()
    created_at= models.DateTimeField()

    def __str__(self):
        return f'[{self.pk}]{self.tag}'