from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Question
from django.template import loader
# Create your views here.

def index(request):
    question_list = Question.objects.order_by('pub_date')
    output = ""
    for q in question_list:
        output = ",".join([q.question_text for q in question_list])
    template = loader.get_template('polls/index.html')
    context = {
        'question_list':question_list,
    }
    return HttpResponse(template.render(context,request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return HttpResponse("You're looking at question %s."%question.question_text)


def results(request,question_id):
    return HttpResponse("You're looking at the result of question %s."%question_id)


def vote(request,question_id):
    return HttpResponse("You're voting a question %s."%question_id)