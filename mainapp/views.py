from django.shortcuts import render
from django.views.generic import TemplateView


class mainTemplateView(TemplateView):
    template_name = 'mainapp/home.html'