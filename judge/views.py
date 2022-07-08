from django.shortcuts import render, HttpResponse, get_object_or_404
from judge.models import  Problems, Solutions
import os, filecmp

# Create your views here.

def problems(request):
    problems_list = Problems.objects.all()
    context = {"Problems_list": problems_list}
    return render(request, "problems_list.html", context)

def problem_detail(request, problem_id):
    problem = get_object_or_404(Problems, id = problem_id)
    return render(request, 'problem_detail.html', {'problem': problem})




