import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    # filter for emp_id range
    emp_id_min = django_filters.CharFilter(field_name="emp_id", lookup_expr="gte")
    emp_id_max = django_filters.CharFilter(field_name="emp_id", lookup_expr="lte")

    # filter for salary range
    salary_min = django_filters.NumberFilter(field_name="salary", lookup_expr="gte")
    salary_max = django_filters.NumberFilter(field_name="salary", lookup_expr="lte")

    class Meta:
        model = Employee
        fields = ['name', 'designation', 'emp_id_min', 'emp_id_max', 'salary_min', 'salary_max']