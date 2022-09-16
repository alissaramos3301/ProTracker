from django.db import models
from django.conf import settings
USER_MODEL = settings.AUTH_USER_MODEL


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=True)
    project = models.ForeignKey("projects.Project",
                                related_name=("tasks"),
                                on_delete=models.CASCADE)
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name=("tasks"),
        on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


# Create your models here.
