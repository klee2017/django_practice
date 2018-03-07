import re

from django.forms import ValidationError
from django.db import models


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn')
    )

    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, help_text='please enter the post title. max length : 100 characters.')
    content = models.TextField()
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True,
                              validators=[lnglat_validator],
                              help_text='longitude/latitude format insert')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
