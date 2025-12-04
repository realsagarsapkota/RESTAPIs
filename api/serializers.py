from rest_framework import serializers
from .models import Employee
# used regular expression  for checking emp_id format
import re

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


    # For email validation
    def validate_email(self, value):
        if not value.endswith('@company.com'):
            raise serializers.ValidationError("Email must end with @company.com")
        return value


    # For salary validation
    def validate_salary(self, value):
        if value <= 0:
            raise serializers.ValidationError("Salary must be in positive integer ")
        return value
        

    # For employee id validation
    def validate_emp_id(self, value):
        if not re.match(r'^EMP[0-9]+$', value):
            raise serializers.ValidationError("emp_id should look like EMP123")
        return value


