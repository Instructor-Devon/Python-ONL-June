from django.shortcuts import render, redirect, HttpResponse
from .models import User, Post, Vote
import re
import bcrypt
from django.contrib.messages import error


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
    user_is_ok = User.objects.authenticate(request.POST["email"], request.POST["password"])

    if user_is_ok:
        # get user's id with email
        user = User.objects.get(email=request.POST['email'])
        request.session["user_id"] = user.id
        return redirect("/dashboard")

    if not user_is_ok:
        error(request, "Invalid Email/Password", extra_tags="login")
        return redirect("/")


def register(request):
    # VALIDATE form input
    # valid email (regex)

    errors = User.objects.validate(request.POST)

    # TODO: DETERMINE if the submission is entirely valid/invalid DONE
    if errors:
        for e in errors:
            error(request, e, extra_tags="reg")
        return redirect("/")
    
    # IF NO ERRORS
    # create our user! (.register returns User object!)
    newUser = User.objects.register(request.POST)

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
        "posts": Post.objects.all().order_by('-updated_at')
    }
    return render(request, "home/dashboard.html", context)

def create(request):
    user = user_in_session(request)
    # VALIDATE form inputs....
    errors = Post.objects.validate(request.POST)

    if errors:
        for e in errors:
            error(request, e)
    else:
        # make a post!
        Post.objects.create(
            topic = request.POST["topic"],
            content = request.POST["content"],
            author = user
            # author_id = request.session["user_id"] (you can do this too)
        )

    return redirect("/dashboard")

def update(request):
    user = user_in_session(request)
    # VALIDATE form inputs....
    errors = Post.objects.validate(request.POST)

    if errors:
        for e in errors:
            error(request, e)
    else:
        # get the post!
        to_update = Post.objects.get(id=request.POST["post_id"])
        if to_update.author != user:
            return redirect("/dashboard")
        # update new fields on post
        to_update.topic = request.POST['topic']
        to_update.content = request.POST['content']
        to_update.save()
        return redirect("/dashboard")

    # TODO: request.POST["post_id"] is vulnerable to HTML manipulation
    return redirect(f"/post/edit/{request.POST['post_id']}")


def delete(request, post_id):
    # get the post
    to_delete = Post.objects.get(id=post_id)
    # make sure that to_delete.author_id == request.session["user_id"]
    if to_delete.author_id == request.session["user_id"]:
        # .delete() the thing
        to_delete.delete()
    return redirect("/dashboard")

def edit(request, post_id):
    # get the post
    to_edit = Post.objects.get(id=post_id)
    # send that post to a template in context:
    context = {
        "post": to_edit
    }
    # redirect all the hackers
    if to_edit.author_id != request.session["user_id"]:
        # .delete() the thing
        return redirect("/dashboard")

    return render(request, "home/edit.html", context)

def vote(request, post_id, is_upvote):
    print(post_id, int(is_upvote)==1)
    Vote.objects.create(
        post_id = post_id,
        voter_id = request.session["user_id"],
        is_upvote = int(is_upvote)==1,
    )
    return redirect("/dashboard")