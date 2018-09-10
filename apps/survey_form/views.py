# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    return render(request,'survey_form/index.html')

def process(request):
    request.session['first_name'] = request.POST['first_name']
    request.session['last_name'] = request.POST['last_name']
    request.session['language'] = request.POST['language']
    request.session['location'] = request.POST['location']
    request.session['comments'] = request.POST['comments']
    
    return redirect('/result')

def result(request):

    return render(request, 'survey_form/result.html', )



# Create your views here.
