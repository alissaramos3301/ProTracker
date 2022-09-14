from django.views.generic.list import ListView
from projects.models import Project


class ProjectListView(ListView):
    model = Project
    template_name = "list.html"
