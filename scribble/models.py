from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class Comment(models.Model):
    Post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100, default='SOME STRING')
    body = models.CharField(max_length=1000, default='SOME STRING')
