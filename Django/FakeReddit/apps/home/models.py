from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    # email needs to be unique! (will be used for logging in)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # posts => [{Post}]

    def __str__(self):
        return self.email

class Post(models.Model):
    topic = models.CharField(max_length=45)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author_id
    author = models.ForeignKey(User, related_name="posts")