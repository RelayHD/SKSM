from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    content= models.TextField()
    created_at= models.DateTimeField()
    first_image= models.ImageField(blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'


class PostImages(models.Model):
    post= models.ForeignKey(Post, related_name="images", default=None, on_delete= models.CASCADE)
    image= models.ImageField(upload_to='main/images/%Y/%m/%d/', blank=True)
    
    def __str__(self):
        return f'[{self.post.pk}]{self.post.title}'
