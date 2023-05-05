from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, TemplateView

from .models import *


def test(request):
    return HttpResponse("<h1>Test</h1>")


class Home(TemplateView):
    template_name = 'menu_view/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['menu'] = TreeNodeModel.objects.all()
        # print(context['menu'][2].level)
        context['menu1'] = TreeNodeModel.objects.filter(number_menu=1)
        context['menu2'] = TreeNodeModel.objects.filter(number_menu=2)
        return context


class Menu(DetailView):
    model = TreeNodeModel
    template_name = 'menu_view/menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context["object"].level)
        number = context["object"].number_menu
        context['menu'] = TreeNodeModel.objects.filter(number_menu=number)
        print(context['menu'][0].get_absolute_url())
        return context
