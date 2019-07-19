from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):

    def validate(self, form):
        errors = []

        if not EMAIL_REGEX.match(form["email"]):
            errors.append("Invalid Email")
        # non-empty inputs for first_name/last_name/email/password
        if len(form["first_name"].strip()) < 1:
            errors.append("First Name field is required")
        if len(form["last_name"].strip()) < 1:
            errors.append("Last Name field is required")
        # password must be 6-10 characters
        if len(form["password"].strip()) > 10 or len(form["password"]) < 6 :
            errors.append("Password must be 6-10 characters")
        # password and confirm must match
        if form["password"].strip() != form["confirm"].strip():
            errors.append("Passwords do not match!")
        # ONE MORE!!! uniqueness of email
        if len(self.filter(email=form["email"])) > 0:
            errors.append("Email is in use")
            print(form, "is data inside manager class")

        return errors

    def register(self, form):
        hashed = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt())

        # create a new user, hashing the password
        return self.create(
            first_name = form['first_name'],
            last_name = form['last_name'],
            email = form['email'],
            password = hashed
        )

    def authenticate(self, email, password):
        """ authenticate user's login submission => bool"""
        # 1) email must be in database
        users_with_email = self.filter(email=email)
        if users_with_email:
            user = users_with_email[0]
            # 2) if email is in db, password from form must match password in db
            return bcrypt.checkpw(password.encode(), user.password.encode())
        return False

    # self.all() => get all Users
    # self.filter(query) => get some Users with query
    # self.create(kwargs) => create one User

class PostManager(models.Manager):
    def validate(self, form):
        # make sure Topic is not empty
        errors = []
        if form["topic"].strip() == "":
            errors.append("Topic is required")
        if len(form["content"].strip()) < 10:
            errors.append("Your post must be at least 10 characters")
        # make sure post is at least 10 characters
        return errors


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    # email needs to be unique! (will be used for logging in)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)

    objects = UserManager()
    
    # votes_given

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
    # votes_received
    objects = PostManager()

    def karma(self):
        num_up = self.votes_received.filter(is_upvote=True) # [Vote, Vote]
        num_down = self.votes_received.filter(is_upvote=False) # [Vote, Vote]
        return len(num_up) - len(num_down)

class Vote(models.Model):
    is_upvote = models.BooleanField()
    post = models.ForeignKey(Post, related_name="votes_received")
    voter = models.ForeignKey(User, related_name="votes_given")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)