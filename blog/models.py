from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from time import time
from django.utils import timezone
from datetime import datetime

from solo.models import SingletonModel

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(verbose_name='Title', max_length=100, db_index=True)
    img = models.FileField(verbose_name='Image', blank=True, upload_to="posts/", default='posts/hegel_pink.jpg')
    body = models.TextField(verbose_name='Body', db_index=True)
    subtitle = models.TextField(verbose_name='Sub title', max_length=150, blank=True)
    date_pub = models.DateTimeField(verbose_name='Date publication', auto_now_add=True)
    date_upd = models.DateTimeField(verbose_name='Date update', blank=True, null=True, default=datetime.now())
    status = models.CharField(verbose_name='Status publication', max_length=10, choices=STATUS_CHOICES, default='draft')
    nav_status = models.BooleanField(verbose_name='Nav bar', default=False)
    slug = models.SlugField(verbose_name='Slug', max_length=150, blank=True, unique=True, db_index=True)

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
        verbose_name = "Blog"

class BlogConfiguration(SingletonModel):
    site_name = models.CharField(verbose_name='Site name', max_length=100, default='cool.site')
    copyright = models.CharField(verbose_name='Copyright', max_length=180, default='copyright')
    main_title = models.CharField(verbose_name='Main title', max_length=50, default='Hello')
    main_subtitle = models.CharField(verbose_name='Main sub title', max_length=100, default='Blog Dev')
    main_img = models.ImageField(verbose_name='Main image', upload_to='posts/')

    def __str__(self):
        return "Blog Configuration"

    class Meta:
        verbose_name = "Blog Configuration"