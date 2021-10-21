from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Frog, Toy
from .forms import FeedingForm

class FrogCreate(CreateView):
    model = Frog
    fields = '__all__' # or fields = ['name', 'species', 'description', 'age']
    succes_url = '/frogs/'

class FrogUpdate(UpdateView):
    model = Frog
    fields = ['species', 'description', 'age']

class FrogDelete(DeleteView):
    model = Frog
    success_url = '/frogs/'

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def frogs_index(request):
    frogs = Frog.objects.all()
    return render(request, 'frogs/index.html', {
        'frogs': frogs
    })

def frogs_detail(request, frog_id):
      frog = Frog.objects.get(id=frog_id)
      toys_frog_doesnt_have = Toy.objects.exclude(id__in = frog.toys.all().values_list('id'))
      feeding_form = FeedingForm()
      return render(request, 'frogs/detail.html',{
        'frog': frog, 'feeding_form': feeding_form,
        'toys': toys_frog_doesnt_have
      })

def add_feeding(request, frog_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.frog_id = frog_id
        new_feeding.save()
    return redirect('detail', frog_id=frog_id)

def assoc_toy(request, frog_id, toy_id):
      # Note that you can pass a toy's id instead of the whole object
  Frog.objects.get(id=frog_id).toys.add(toy_id)
  return redirect('detail', frog_id=frog_id)

class ToyList(ListView):
      model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'
