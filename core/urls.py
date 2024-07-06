from django.contrib import admin
from django.urls import path
from app.views import book_list, book_detail, book_create, book_update, book_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_list, name='book_list'),
    path('detail/<int:pk>/', book_detail, name='book_detail'),
    path('create/', book_create, name='book_create'),
    path('update/<int:pk>/', book_update, name='book_update'),
    path('delete/<int:pk>/', book_delete, name='book_delete')
]
