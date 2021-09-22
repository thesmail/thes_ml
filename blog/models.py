from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
from django.utils import timezone
from datetime import datetime

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

class Post(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    img = models.FileField(blank=True, upload_to="posts/", default='posts/hegel_pink.jpg')
    body = models.TextField(db_index=True)
    quo = models.TextField(max_length=150, blank=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(blank=True, null=True, default=datetime.now())
    nav_status = models.BooleanField(default=False)
    slug = models.SlugField(max_length=150, blank=True, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)

        self.date_upd = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['-date_pub']