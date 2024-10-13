from django.urls import path
from .views import ProjectListCreateView

app_name = "project"
urlpatterns = [
    path('', ProjectListCreateView.as_view(), name='project-list-create'),
]
