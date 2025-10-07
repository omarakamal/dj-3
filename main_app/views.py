from django.shortcuts import render
from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action  # <-- must be present
from rest_framework.response import Response

# Create your views here.



def home(request):

    return render(request, 'home.html')



class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer


    
    @action(detail=False, methods=['post'], url_path='bulk-create')
    def bulk_create(self, request):
        """
        POST /students/bulk-create/
        Accepts a list of student objects for bulk insertion.
        """
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_bulk_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_bulk_create(self, serializer):
        serializer.save()

