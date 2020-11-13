from django.shortcuts import render

from authapp.forms import LoginForm


def login(request):
    form = LoginForm()

    context = {
        'form': form,
        'page_title': 'авторизация',
    }
    return render(request, 'authapp/login.html', context)
