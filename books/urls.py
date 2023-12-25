from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("books/<int:pk>/", views.book_detail, name="book_detail"),
    path("books/<int:pk>/add_review/", views.submit_review, name="submit_review"),
]
