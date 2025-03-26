from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('',views.book_list, name="book-list"),
    path('insert',views.insert_book, name="insert-book"),
    path('<int:pk>/',views.view_book, name="view-book"),   
    path('<int:pk>/edit/',views.edit_book, name="edit-book"),   
    path('<int:pk>/delete/',views.delete_book, name="delete-book"),   
]