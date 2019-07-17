from django.shortcuts import render, redirect, HttpResponse
from .models import User, Post
import re
import bcrypt
from django.contrib.messages import error

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def user_in_session(request):
    ''' returns User if someone is logged in.  None if not '''
    if not "user_id" in request.session:
        return None
    user = User.objects.get(id=request.session["user_id"])
    return user

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def logout(request):
    request.session.clear()
    return redirect("/")

def login(request):
    # VALIDATE form input
    user_is_ok = True

    # 1) email must be in database
    # user_check => [{User}] OR []
    user_check = User.objects.filter(email=request.POST["email"])

    if user_check:
        # {User}
        user = user_check[0]
        
        # 2) if email is in db, password from form must match password in db
        valid_password = bcrypt.checkpw(request.POST["password"].encode(), user.password.encode())
        if not valid_password:
            user_is_ok = False
        else:
            # USER IS GOOD TO GO!
            # store id in session
            request.session["user_id"] = user.id
            # redirect to success
            return redirect("/dashboard")
    else:
        user_is_ok = False
            

    if not user_is_ok:
        error(request, "Invalid Email/Password", extra_tags="login")
        return redirect("/")


def register(request):
    # VALIDATE form input
    # valid email (regex)

    errors = []

    if not EMAIL_REGEX.match(request.POST["email"]):
        errors.append("Invalid Email")
    # non-empty inputs for first_name/last_name/email/password
    if len(request.POST["first_name"]) < 1:
        errors.append("First Name field is required")
    if len(request.POST["last_name"]) < 1:
        errors.append("Last Name field is required")
    # password must be 6-10 characters
    if len(request.POST["password"]) > 10 or len(request.POST["password"]) < 6 :
        errors.append("Password must be 6-10 characters")
    # password and confirm must match
    if request.POST["password"] != request.POST["confirm"]:
        errors.append("Passwords do not match!")
    # ONE MORE!!! uniqueness of email
    if len(User.objects.filter(email=request.POST["email"])) > 0:
        errors.append("Email is in use")

    # TODO: DETERMINE if the submission is entirely valid/invalid DONE
    if errors:
        for e in errors:
            error(request, e, extra_tags="reg")
        return redirect("/")
    
    # IF NO ERRORS
    # TODO: hash user's password
    hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    # create our user! (.create returns User object!)
    newUser = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = hashed
    )


    # TODO: store user_id in SESSION DONE
    request.session["user_id"] = newUser.id
    return redirect("/dashboard")

def dashboard(request):
    # only logged in users should be here!
    user = user_in_session(request)
    if not user:
        return redirect("/")
    context = {
        "user": user,
        "posts": Post.objects.all()
    }
    return render(request, "home/dashboard.html", context)

def create(request):
    user = user_in_session(request)
    # VALIDATE form inputs....

    # make a post!
    Post.objects.create(
        topic = request.POST["topic"],
        content = request.POST["content"],
        author = user
        # author_id = request.session["user_id"] (you can do this too)
    )

    return redirect("/dashboard")
