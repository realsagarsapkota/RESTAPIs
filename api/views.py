from django.shortcuts import render
# from rest_framework.views import APIView
from .models import Employee
from django.shortcuts import get_object_or_404
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status, mixins, generics, viewsets
from .pagination import EmployeePageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import EmployeeFilter


#------------------------ Start of APIview-------------------------------------!
# class EmployeeListCreateView(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EmployeeDetailView(APIView):
#     def get(self, request, pk):
#         employee = get_object_or_404(Employee, pk=pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         employee = get_object_or_404(Employee, pk=pk)
#         serializer = EmployeeSerializer(employee, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         employee = get_object_or_404(Employee, pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#------------------------ End of APIview-------------------------------------!

# -------------------------Start of Mixins--------------------------------!

# class EmployeesList(mixins.ListModelMixin, mixins.CreateModelMixin ,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)
    
# class EmployeeDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#         queryset = Employee.objects.all()
#         serializer_class = EmployeeSerializer

#         def get(self, request, pk):
#             return self.retrieve(request, pk)
        
#         def put(self, request, pk):
#             return self.update(request, pk)
        
#         def delete(self, request, pk):
#             return self.delete(request, pk)

# ...............End of Mixins--------------------------------------------


# ........................ Start of Generic View..............................

# class EmployeesList(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# ---------------------End of Generic View-------------------------------------




# ...........................Start of ViewSet----------------------------------
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = EmployeePageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'designation']
    filterset_class = EmployeeFilter

