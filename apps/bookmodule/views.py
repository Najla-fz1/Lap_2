from django.http import HttpResponse
from django.shortcuts import render 
from .models import Book
from django.db.models import Q




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


def add_data(request):
    mybook1 = Book(title='Continuous Delivery', author='J.Humble and D. Farley', edition=1)
    mybook1.save()
    mybook2 = Book.objects.create(title='Continuous Delivery', author='J.Humble and D. Farley', edition=1)
    mybook2.save()
    return HttpResponse("Data added successfully")

 
def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})


def complex_query(request):
    mybooks=books=Book.objects.filter(
        author__isnull = False).filter(
            title__icontains='and')
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    

def task1(request):
    mybooks = Book.objects.filter(Q(price__lt=80) | Q(price=80))
    return render(request, 'task1.html', {'books': mybooks})

def task2(request):
    mybooks = Book.objects.filter(
        Q(edition__gt=3) &
        (Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'task2.html', {'books': mybooks})


def task3(request):
    mybooks = Book.objects.filter(
        Q(edition__lt=3) &
        ~(Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'task3.html', {'books': mybooks})


def task4(request):
    mybooks = Book.objects.all().order_by('title')
    return render(request, 'task4.html', {'books': mybooks})


from django.db.models import Count, Sum, Avg, Max, Min

def task5(request):
    aggregation = Book.objects.aggregate(
        count=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'task5.html', {'aggregation': aggregation})



from .models import Department, Course, Student11 , Card



def delete_all_data(request):
    Book.objects.all().delete()
    Department.objects.all().delete()
    Course.objects.all().delete()
    Card.objects.all().delete()
    Student11.objects.all().delete()
    return HttpResponse("تم حذف جميع البيانات بنجاح")



# Task 1
def task11(request):
    departments = Department.objects.annotate(student_count=Count('student11'))
    return render(request, 'task1.html', {'departments': departments})

# Task 2
def task22(request):
    courses = Course.objects.annotate(student_count=Count('student11'))
    return render(request, 'task2.html', {'courses': courses})

# Task 3
def task33(request):
    departments = Department.objects.all()
    result = []

    for dept in departments:
        student = Student11.objects.filter(student_Department=dept).order_by('id').first()
        if student:
            result.append((dept.name, student.name))

    return render(request, 'task3.html', {'result': result})


# Task 4
def task44(request):
    departments = Department.objects.annotate(student_count=Count('student11'))
    departments = departments.filter(student_count__gt=2).order_by('-student_count')
    return render(request, 'task4.html', {'departments': departments})









