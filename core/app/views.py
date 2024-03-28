from django.shortcuts import render
from django.views.generic import TemplateView
from .mixins import CustomMixin

class TestView(CustomMixin, TemplateView):
    template_name = 'app/test.html'