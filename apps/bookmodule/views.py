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

def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links_page(request):
    return render(request, 'links.html')

def text_formatting(request):
    return render(request, 'formatting.html')

def listing(request):
    return render(request, 'listing.html')

def tables(request):
    return render(request, 'tables.html')

# def search(request):
#     return render(request, 'search.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def search(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        filtered_books = []

        for book in books:
            match = False
            if isTitle and keyword in book['title'].lower():
                match = True
            if not match and isAuthor and keyword in book['author'].lower():
                match = True
            
            if match:
                filtered_books.append(book)

        return render(request, 'bookList.html', {'books': filtered_books})
    
    return render(request, 'search.html')    

 








