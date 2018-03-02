from django.http import HttpResponse


def mysum(request, numbers):
    # splited = numbers.split('/')
    # print(splited)
    number = map(lambda x: int(x or 0), numbers.split('/'))
    return HttpResponse(sum(number))

def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name, age))
