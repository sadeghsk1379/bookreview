from django.shortcuts import render, redirect
from .models import Book, Review
from .forms import ReviewForm


def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    reviews = book.review_set.all()

    # Calculate average rating
    ratings = []
    for review in reviews:
        ratings.append(review.rating)

    if len(ratings) > 0:
        average_rating = sum(ratings) / len(ratings)
    else:
        average_rating = None

    return render(
        request, "book_detail.html", {"book": book, "average_rating": average_rating}
    )


def submit_review(request, pk):
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.book = Book.objects.get(pk=pk)
        review.save()
        return redirect("book_detail", pk=pk)
    else:
        form = ReviewForm()
        return render(request, "submit_review.html", {"form": form})
