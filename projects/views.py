from django.views.generic.list import ListView
from projects.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "list.html"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "detail.html"


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "create.html"
    fields = ["name", "description", "members"]

    def get_success_url(self):
        return reverse_lazy("show_project", args=[self.object.id])
