# Add the Cat class & list and view function below the imports
class Frog:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, species, description, age):
    self.name = name
    self.species = species
    self.description = description
    self.age = age

frogs = [
  Frog('Lolo', 'poison dart', 'innocent killer', 3),
  Frog('Sachi', 'kermit', 'big ribbit', 0),
  Frog('Raven', 'black tiller', 'spotted toad', 4)
]

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Home</h1>')

def about(request):
    return render(request, 'about.html')

def frogs_index(request):
    return render(request, 'frogs/index.html', {
        'frogs': frogs
    })
