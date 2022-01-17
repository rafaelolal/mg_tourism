"""The most basic views"""

from django.views.generic import TemplateView
from django.shortcuts import render

class IndexView(TemplateView):
    template_name = 'core/index.html'

class FeaturesView(TemplateView):
    template_name = 'core/features.html'

class DocsView(TemplateView):
    template_name = 'core/docs.html'