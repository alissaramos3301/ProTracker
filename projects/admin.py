from django.contrib import admin
from projects.models import Project
from tasks.models import Task


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)


class TaskAdmin(admin.ModelAdmin):
    pass


admin.site.register(Task, TaskAdmin)
