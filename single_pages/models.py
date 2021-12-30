from django.db import models

class SinglePost(models.Model):
    tag= models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    paragraph_1= models.TextField(blank=True, null=True)
    paragraph_2= models.TextField(blank=True, null=True)
    paragraph_3= models.TextField(blank=True, null=True)
    paragraph_4= models.TextField(blank=True, null=True)
    created_at= models.DateTimeField()

    def __str__(self):
        return f'[{self.pk}] {self.tag}'