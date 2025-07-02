from django.urls import path 
from . import views
urlpatterns = [
    path('', views.show_photography, name='photography_list'),
    path('create/', views.create_photography, name='new_photography'),
    path('<int:pk>/view/', views.view_photography, name='show_photography'),
    path('<int:pk>/edit/', views.edit_photography, name='update_photography'),
    path('<int:pk>/delete/', views.delete_photography, name='remove_photography'),
]