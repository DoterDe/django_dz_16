from django.shortcuts import render
from .models import Book
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.generic import ListView , CreateView , UpdateView, DeleteView


def home(request):
    books = Book.objects.all()
    paginator= Paginator(books, 2)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    return render(request, 'home.html', {'page':page_obj})

class BookList(ListView):
    model = Book
    paginate_by = 2
    template_name = 'home.html'

class CreateBook(CreateView):
    model = Book
    fields = ['title', 'description', 'author', 'published_year', 'price','genre']
    success_url = reverse_lazy('home')
    template_name = 'create.html'

class DeleteBook(DeleteView):
    model =Book
    success_url = reverse_lazy('home')
    template_name = 'delete.html'

class UpdateBook(UpdateView):
    model =Book
    fields = ['title', 'description', 'author', 'published_year', 'price','genre']
    success_url = reverse_lazy('home')
    template_name_suffix = "_update_form"
    template_name = 'update.html'