from django.http import HttpResponse
from django.shortcuts import render


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
