from django.shortcuts import render, redirect
from .models import Book
def index(request):
    return render(request, "home/index.html", {
        "books": Book.objects.all()
    })

def create(request):
    Book.objects.create(
        title = request.POST["title"],
        description = request.POST["description"],
        pub_date = request.POST["pub_date"],
    )
    return redirect("/")
