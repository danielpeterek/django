from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from bazar.models import Tenisky


def index(request):
    context = {
        'nadpis': 'Web o teniskách',
    }

    return render(request, template_name='index.html', context=context)


class SneakersListView(ListView):
    model = Tenisky
    context_object_name = 'tenisky_list'
    template_name = 'list.html'


class SneakersDetailView(DetailView):
    model = Tenisky
    context_object_name = 'tenisky'
    template_name = 'detail.html'


class TeniskyCreate(CreateView):
    model = Tenisky
    fields = ['nazev','popis','velikost','cena','cena1','foto']
    initial = {'cena': 500}


class TeniskyUpdate(UpdateView):
    model = Tenisky
    fields = '__all__' # Not recommended


class TeniskyDelete(DeleteView):
    model = Tenisky
    success_url = reverse_lazy('list')

