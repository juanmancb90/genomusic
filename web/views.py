# Python Modules
import json

# Django Modules
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

# App Modules
from sequencer.utils import search


def index(request):
    context = {}
    return render(request, 'web/index.html', context)


def search_sequence(request):
    name = request.POST.get('name', None)
    db = request.POST.get('db', None)
    if name is None or db is None:
        return HttpResponseBadRequest('error')
    data = json.dumps(search(name, db))
    return HttpResponse(data)
