from django.shortcuts import render

from studentapp.models import Student


def student(request):
    students = Student.objects.all()
    more = Student.objects.get()
    context = {
        'students': students,
        'more': more,
        'page_title': 'студенты',
    }

    return render(request, 'studentapp/student.html', context)
