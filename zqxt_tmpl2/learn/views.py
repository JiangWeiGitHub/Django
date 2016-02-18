from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    TutorialList = ["Rice", "Noodle", "Spring roll", "Steamed Stuffed Bun", "Dumpling"]
    return render(request, 'home.html', {'TutorialList': TutorialList})
