from django.shortcuts import render

from studentapp.models import Student


def student(request):
    students = Student.objects.all()
    context = {
        'students': students,
        'page_title': 'студенты',
    }

    return render(request, 'studentapp/student.html', context)
