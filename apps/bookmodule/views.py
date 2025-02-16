from django.http import HttpResponse
from django.shortcuts import render 


def index(request):
    # 'name' variable has a default value of 'world' 
    # if not provided in the URL query parameters
    name = request.GET.get('name', 'world')
    # Returns a response with a greeting message
    # including the provided or default name
    return HttpResponse("Hello, "+str(name))

def index2(request, val1 = 0):
    try:
        int_val = int(val1)
        return HttpResponse("value1 = "+str(val1))
    except ValueError:
        return HttpResponse("error, expected val1 to be integer")

def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodule/show.html', context)
