from django.shortcuts import render, HttpResponse, redirect
from django.contrib.messages import error
from .models import PartyPerson, Party
# Create your views here.
def index(request):
    context = {
        "people": PartyPerson.objects.all(),
        "parties": Party.objects.all()
    }
    return render(request, 'party/index.html', context)

def create_user(request):
    # make a call to PartyPerson.objects.validate()

    # for now well do them here
    # validate name field
    errors = PartyPerson.objects.validate(request.POST)    

    # check if errors:
    if errors:
        for err in errors:
            error(request, err)
    else:
        # make a guy!
        PartyPerson.objects.create(name=request.POST['name'], birthday=request.POST['birthday'])
    return redirect('/')
    

def create_party(request):
    # we need name, location, host (user.id)
    person = PartyPerson.objects.get(id=request.POST['host'])
    Party.objects.create(
        name = request.POST['name'],
        location = request.POST['location'],
        host = person, # host => ID!!!!!
    )
    return redirect("/")