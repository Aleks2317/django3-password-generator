

from django.shortcuts import render
from django.http import HttpResponse
import random




def home(requests):
    return render(requests, 'generator/home.html')


def password(requests):

    characters = list('abcdefghijklmnoprstuvwxyz')

    length = int(requests.GET.get('length', 12))

    if requests.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIKLMNOPRSTUVWXYZ'))

    if requests.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if requests.GET.get('numbers'):
        characters.extend(list('0123456789'))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(requests, 'generator/password.html', {'password':thepassword})

def info(requests):
    return render(requests, 'generator/about.html')


