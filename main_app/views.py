from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Frog
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
    return HttpResponse('<h1>Home</h1>')


def about(request):
    return render(request, 'about.html')


def frogs_index(request):
    frogs = Frog.objects.all()
    return render(request, 'frogs/index.html', {
        'frogs': frogs
    })

def frogs_detail(request, frog_id):
      frog = Frog.objects.get(id=frog_id)
      feeding_form = FeedingForm()
      return render(request, 'frogs/detail.html',{
        'frog': frog, 'feeding_form': feeding_form
      })

def add_feeding(request, frog_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.frog_id = frog_id
        new_feeding.save()
    return redirect('detail', frog_id=frog_id)
