from django.shortcuts import render
from .models import Question
# Create your views here.
from django.shortcuts import get_object_or_404, render

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'details.html', {'question': question})