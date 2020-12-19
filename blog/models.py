from django.db import models
from django.shortcuts import reverse

class Post(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=150, db_index=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug'})

    def __str__(self):
        return '{}'.format(self.title)