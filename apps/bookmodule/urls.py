from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    # path('index2/<int:val1>/', views.index2)
    path('index2/<str:val1>/', views.index2, name="book_index2"),
    path('<int:bookId>', views.viewbook)
]
