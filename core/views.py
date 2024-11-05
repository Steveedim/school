from django.shortcuts import render
from .models import Class, Student

# Create your views here.
def home(request):
    students = Student.objects.all()

    context = {"students": students}
    return render(request, 'core/home.html', context)
