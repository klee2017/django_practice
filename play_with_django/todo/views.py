from django.http import HttpResponse


def mysum(request, numbers):
    # splited = numbers.split('/')
    # print(splited)
    number = map(lambda x: int(x or 0), numbers.split('/'))
    return HttpResponse(sum(number))
