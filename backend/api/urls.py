from django.urls import path
from . import views


urlpatterns = [
    path('check/', views.TaskView.as_view(), name='check-url'),
]