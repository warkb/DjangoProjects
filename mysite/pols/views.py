from django.shortcuts import render
from django.http import HttpResponse

from django.template import RequestContext, loader
from .models import Question
# Create your views here.
string = "All good"

def index(request):
    #отобразить 5 последних вопросов разделенных
    #запятой от самого нового к самому старому
    latest_question_list = Question.objects.order_by(
        '-pub_date')[:5]
    template = loader.get_template('pols/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
        })
    context = {'latest_question_list': latest_question_list,}
    #return HttpResponse(str(latest_question_list))
    return HttpResponse(template.render(context))

def detail(request, question_id):
    return HttpResponse("Вопрос: %s" % question_id)

def results(request, question_id):
    response = "Результаты вопроса %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Вы голосуете по вопросу %s" % 
        question_id)
