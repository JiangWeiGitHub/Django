#from django.shortcuts import render

# Create your views here.

#coding:utf-8
#from django.http import HttpResponse
#from django.shortcuts import render

#def home(request):
#    string = u"indeed a good day!!!"
#    myList = map(str, range(100))
#    return render(request, 'home.html', {'myList': myList})
 
#def index(request, a, b):
    #a = request.GET.get('a', 0)
    #b = request.GET.get('b', 0)
#    c = int(a) + int(b)
#    return HttpResponse(u"Welcome to my site!" + " a + b = "  + str(c))

# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

from .forms import AddForm
 
def index(request):
    if request.method == 'POST':
     
        form = AddForm(request.POST)
         
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
     
    else:
        form = AddForm()
    return render(request, 'index.html', {'form': form})


