from . import views
from django.urls import path

urlpatterns = [
    path('users/', views.AllUsersView.as_view(), name='users'),
]