from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    my_context = {
        'my_t': 'this is c',
        'my_t1': 'this is c1',
        'my_list': [111, 222, 333]
    }

    # return HttpResponse('<h1>Test</h1>')
    return render(request, 'home.html', my_context)
