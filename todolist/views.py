from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    text = "<h1>neki drugi tekst za test</h1>"
    return HttpResponse(text)
    #return render(request, "base.html", {"todo_list": todos})
