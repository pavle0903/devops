from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    text = "<h1>Welcome to my app</h1>"
    return HttpResponse(text)
    #return render(request, "base.html", {"todo_list": todos})
