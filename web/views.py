# Django Modules
from django.shortcuts import render

# App Modules
from sequencer.utils import search


def index(request):
    context = {}
    return render(request, 'web/index.html', context)


def search_sequence(request):
    pass
