from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    string = u"DJango is not funny!"
    return render(request, 'home.html', {'string':string})

