from django.shortcuts import render
from django.views.generic import ListView

from todo.models import User


# Create your views here.
class AllUsersView(ListView):
    model = User
    template_name = 'todo/users.html'