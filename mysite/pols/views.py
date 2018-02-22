from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from django.template import RequestContext, loader
from .models import Question
from django.urls import reverse
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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'pols/detail.html', {'question': question})

def results(request, question_id):
    response = "Результаты вопроса %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'pols/detail.html', {
            'question': question,
            'error_message': 'Ты не сделал выбор'
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponse(reverse('pols:results', args=(question.id)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'pols/results.html', {'question': question})