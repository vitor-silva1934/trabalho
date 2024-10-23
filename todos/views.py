from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Todo


def home(request):
    return render(request, "home.html")

class TodoListView(ListView):
    model=Todo


class TodoCrateView(CreateView):
    model=Todo
fields=["title","deadline"]
success_url=reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'deadline']
    success_url = reverse_lazy('todo_list')



class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')