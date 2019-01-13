from django.shortcuts import render
from django.http import HttpResponse
from my_wbp.apps.main.models import Question


def index(request):
    return render(request,"index.html")
def pools(request):
    quest = Question.objects.all()
    context = {
        'Quests' : quest
    }
    return render(request, "pools.html",context)