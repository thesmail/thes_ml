from django.db import models
from solo.models import SingletonModel

class Link(models.Model):
    l_created = models.DateTimeField(auto_now_add=True)
    l_name = models.CharField(max_length=80, blank=True)
    l_url = models.URLField()
    l_followed = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-l_created"]
        verbose_name = "Link"

    def __str__(self):
        return self.l_url

    # def save(self, *args, **kwargs):
    #     if not self.short_url:
    #         self.short_url = create_shortened_url(self)
    #
    #     super().save(*args, **kwargs)

class Social(models.Model):
    SOCIAL = (
        ('tg', 'telegram'),
        ('fb', 'facebook-f'),
        ('twi', 'twitter'),
        ('ins', 'instagram'),
        ('li', 'linkedin'),
        ('yt', 'youtube'),
        ('git', 'github'),
        ('be', 'behance'),
    )
    s_name = models.CharField(choices=SOCIAL, max_length=4)
    s_url = models.URLField()
    s_followed = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Social"

    def __str__(self):
        return f'{self.s_name} ({self.s_url})'



class TapLinkConfiguration(SingletonModel):
    site_name = models.CharField(max_length=255, default='@thes.ml')
    logo = models.ImageField(upload_to='taplink/')
    note = models.CharField(max_length=255, default='All Links')

    class Meta:
        verbose_name = "TapLink Configuration"

    def __str__(self):
        return "TapLink Configuration"