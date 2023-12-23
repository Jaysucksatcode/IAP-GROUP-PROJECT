from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField(default=1)
    completed = models.BooleanField(default=False)

    class Meta:
        app_label = 'task_tracker'
    def _str_(self):
        return self.title

