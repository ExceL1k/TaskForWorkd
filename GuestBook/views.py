import urllib
import json

from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from ipware.ip import get_ip
from django.conf import settings
from .models import BookGuest
from .tables import *
from django_tables2 import RequestConfig
from django.contrib import messages
from user_agents import parse
# Create your views here.


class BookView(View):
    def get(self, request):
        ObjectsTable = BookTable(BookGuest.objects.all())
        RequestConfig(request, paginate={'per_page': 10}).configure(ObjectsTable)
        return render(request, 'VievTable.html', {'ObjectTables': ObjectsTable})


def comments(request):

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                post = form.save(commit=False)
                post.ip = get_ip(request)
                post.cashBrowser = str(parse(request.META['HTTP_USER_AGENT']))
                post.save()
                messages.success(request, 'New comment added with success!')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')

            return redirect('/')
    else:
        form = BookForm()

    return render(request, 'example.html', {'form': form})
