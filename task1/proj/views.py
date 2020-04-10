from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    #template = loader.get_template("proj/index.html")
    return render(request, 'task1/index.html')#(template.render(request))