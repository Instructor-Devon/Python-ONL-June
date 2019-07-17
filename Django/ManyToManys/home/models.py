from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

    # Many Books that User has favorited
    # favorite_books
    # someUser.favorite_books.add(someBook)


class Book(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    pub_date = models.DateTimeField()

    # Many Users that favorited this book
    fans = models.ManyToManyField(User, related_name="favorite_books")
