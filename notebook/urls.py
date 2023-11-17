from django.urls import path, include
from notebook.views import CategoryListView, BlogPostListView, AuthorListView
urlpatterns = [
    path("", CategoryListView.as_view(), name="category-list"),
    path("blog/", BlogPostListView.as_view(), name="blog-post-list"),
    path("authors/", AuthorListView.as_view(), name="author-list"),
]   