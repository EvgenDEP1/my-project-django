import studentapp.views as studentapp
from django.urls import path

app_name = 'studentapp'

urlpatterns = [
    path('', studentapp.student, name='student'),
]
