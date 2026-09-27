from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    pass

class Post(models.Model):

    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=False)
    author = models.ForeignKey('User', on_delete=models.CASCADE, related_name="posts")
    timestamp = models.DateTimeField(auto_now_add=True)
    isEdited = models.BooleanField(default=False)
    likes = models.ManyToManyField('User', related_name="liked_by", blank=True)
    

    @property
    def formatted_time(self):
        if self.timestamp:
            return self.timestamp.strftime("%d %B at %I%p").lower()
        return "unknown time"

    def __str__(self):
        return f''' {self.author}:

                    {self.content}
                                                            {self.formatted_time}'''

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following") 
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")

    def __str__(self):
        return f"{self.follower} is following {self.following}"
     