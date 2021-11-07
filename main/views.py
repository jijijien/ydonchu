from django.shortcuts import render
from common.models import People
from django.contrib.auth.models import User
from talk.models import Question
from django.db.models import Count
# Create your views here.

def index(request):
    
    username = request.user.username
    question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    question_list=question_list[0:5]
    People_me = {'people':People.objects.get(name=username),'question_list': question_list}
    return render(request, 'main/mainscreen.html',People_me)
