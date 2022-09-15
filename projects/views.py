from django.views.generic.list import ListView
from projects.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "list.html"
