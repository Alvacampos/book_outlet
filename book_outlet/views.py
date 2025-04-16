from django.shortcuts import render
from django.http import Http404
from django.db.models import Avg

from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all().order_by('title')
    num_books = books.count()
    average_rating = books.aggregate(Avg('rating'))
    
    return render(request, 'book_outlet/index.html', 
        {
            'books': books,
            'total_number_of_books': num_books,
            'average_rating': average_rating
        }
    )


def book_detail(request, slug):
    try: 
        book = Book.objects.get(slug=slug)
    except:
        raise Http404("Book does not exist")
    
    return render(request, 'book_outlet/book_detail.html',
        {
            'title': book.title,
            'author': book.author,
            'rating': book.rating,
            'is_bestseller': book.is_bestseller,
            'slug': book.slug,
        }
    )
