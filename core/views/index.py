"""The most basic views"""

from django.views.generic import TemplateView
from django.shortcuts import render

class IndexView(TemplateView):
    template_name = 'core/index.html'

class FeaturesView(TemplateView):
    template_name = 'core/index.html'

def documentation(request):
    return render(request, "_build/html/index.html")