from django.shortcuts import render
from django.http import HttpResponse


def calculate_view(request):
    if request.method=="GET":
        return render(request, "calculate_view.html")
    elif request.method=="POST":
        result = 0
        operator = ''
        try:
            if request.POST['num'] == 'add':
                operator = '+'
                result = int(request.POST['first']) + int(request.POST['second'])
            elif request.POST['num'] == 'subtract':
                operator = '-'
                result = int(request.POST['first']) - int(request.POST['second'])
            elif request.POST['num'] == 'multiply':
                operator = '*'
                result = int(request.POST['first']) * int(request.POST['second'])
            elif request.POST['num'] == 'divide':
                operator = '/'
                result = int(request.POST['first']) / int(request.POST['second'])
        except Exception:
            return HttpResponse('Error choice action')
        message = f"Result:  {request.POST['first']} {operator} {request.POST['second']} = {round(result)}"
        return render(request, 'result_calculate.html', {'message': message})
# Create your views here.
