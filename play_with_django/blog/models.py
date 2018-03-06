from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, help_text='please enter the post title. max length : 100 characters.')
                             # choices=(
                             #     ('title1', 'title1 label'),
                             #     ('title2', 'title2 label'),
                             #     ('title3', 'title3 label'),
                             # )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
