from django.urls import path, include
# from .views import EmployeeListCreateView, EmployeeDetailView 
# from .views import EmployeesList, EmployeeDetail
from .views import EmployeeViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("employees", EmployeeViewSet, basename="employee")

# url patterns
urlpatterns = [
    
    # Urls for classbased APIview
    # path("employees/", EmployeeListCreateView.as_view(), name="employee_list_create"),
    # path("employees/<int:pk>/", EmployeeDetailView.as_view(), name="employee_detail"),

    # Url for mixins and generic api view
    # path("employees/", EmployeesList.as_view(), name="employee_list_create"),
    # path("employees/<int:pk>/", EmployeeDetail.as_view(), name="employee_detail"),

    # Url for viewsets
    path("", include(router.urls)),
    
    
]
