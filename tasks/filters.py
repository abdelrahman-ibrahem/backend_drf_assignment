import  django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    due_date_range = django_filters.DateFromToRangeFilter(
        label= "due date range",
    )
    class Meta:
        model = Task
        fields = [
            "completed",
            "due_date_range",
        ]