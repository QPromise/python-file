from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, world. You\'re at the poll index.')

def detail(request, question_id):
    return HttpResponse(
         'You\'re looking at question {id}.'.format(id = question_id))

def results(request, question_id):
    return HttpResponse(
       'You\'re looking at the results of question {id}.'.format(id = question_id))

def vote(request, question_id):
    return HttpResponse(
      'You\'re voting on question {id}.'.format(id = question_id))
