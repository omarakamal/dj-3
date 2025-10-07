from django.shortcuts import render
from .models import Person
# Create your views here.



def quick_route(request):

    persons = Person.objects.all()

    return render(request,'quick-template.html',{'persons':persons})



def second_route(request):


    return render(request,'second.html')