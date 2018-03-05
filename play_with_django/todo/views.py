import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings


def mysum(request, numbers):
    # splited = numbers.split('/')
    # print(splited)
    number = map(lambda x: int(x or 0), numbers.split('/'))
    return HttpResponse(sum(number))


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name, age))


def post_list1(request):
    name = '공유'
    return HttpResponse('''
        <h1>Django</h1>
        <p>{name}</p>
        <p>장고 연습하기: FBV 직접 문자열로</p>
    '''.format(name=name))


def post_list2(request):
    name = '공유'
    return render(request, 'todo/post_list.html', {'name': name})


def post_list3(request):
    return JsonResponse({
        'message': 'hello, python and django',
        'items': ['Python', 'Django', 'Celery', 'Azure', 'AWS'],
    }, json_dumps_params={'ensure_ascii': False})


def excel_download(request):
    filepath = os.path.join(settings.BASE_DIR, 'gdplev.xls')
    # filepath1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # filepath2 = os.path.join(filepath1, 'gdplev.xls')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachement; filename = "{}"'.format(filename)
        return response
