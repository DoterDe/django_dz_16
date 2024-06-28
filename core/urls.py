
from django.contrib import admin
from django.urls import path
from app.views import home , CreateBook, DeleteBook , UpdateBook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home' ),
    path('create/', CreateBook.as_view(), name='create'),
    path('delete/<int:pk>',DeleteBook.as_view(), name='delete' ),
    path('update/<int:pk>', UpdateBook.as_view(),name= 'update')
]
