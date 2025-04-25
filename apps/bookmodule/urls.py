from django.urls import path
from . import views
# urlpatterns = [
#     path('', views.index),
#     # path('index2/<int:val1>/', views.index2)
#     path('index2/<str:val1>/', views.index2, name="book_index2"),
#     path('<int:bookId>', views.viewbook)
# ]
urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.links_page),
    path('html5/text/formatting', views.text_formatting),
    path('html5/listing', views.listing),
    path('html5/tables', views.tables),
    path('search', views.search),
    path('add_data/', views.add_data),
    path('simple/query/', views.simple_query),
    path('complex/query/', views.complex_query),
    path('lab8/task1', views.task1),
    path('lab8/task2', views.task2),
    path('lab8/task3', views.task3),
    path('lab8/task4', views.task4),
    path('lab8/task5', views.task5),
    # ////// lab 9
    # path('delete-data/', views.delete_all_data),
    path('lab9/task11', views.task11),
    path('lab9/task22', views.task22),
    path('lab9/task33', views.task33),
    path('lab9/task44', views.task44),
    #-------- lab 10 p1 -----------------------------------
    path('lab10_part1/listbooks10', views.list_books10, name='listbooks10'),
    path('lab10_part1/addbook10', views.add_book10, name='addbook10'),
    path('lab10_part1/editbook10/<int:id>', views.edit_book10, name='editbook10'),
    path('lab10_part1/deletebook10/<int:id>', views.delete_book10, name='deletebook10'),
    #-------- lab 10 p2 -----------------------------------
    path('lab10_part2/listbooks10', views.list_books10, name='listbooks10'),
    path('lab10_part2/addbook10', views.add_book10, name='addbook10'),
    path('lab10_part2/editbook10/<int:id>', views.edit_book10, name='editbook10'),
    path('lab10_part2/deletebook10/<int:id>', views.delete_book10, name='deletebook10'),
]

