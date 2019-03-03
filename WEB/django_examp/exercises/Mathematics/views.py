from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def do_math(req, operation, a, b):
    result = None
    a, b = int(a), int(b)
    if operation == 'add':
        result = a + b
    elif operation == 'sub':
        result = a - b
    elif operation == 'mul':
        result = a * b
    elif operation == 'div':
        if b == 0:
            result = "Nie dziel przez zero"
        else:
            result = a/b

    return HttpResponse(result)

# def sub(request,a,b):
#     c = a-b
#     return HttpResponse(f"Wynik: {c}")
#
# def mul(request,a,b):
#     c = a*b
#     return HttpResponse(f"Wynik: {c}")
#
# def dev(request,a,b):
#     c = a/b
#     return HttpResponse(f"Wynik: {c}")
