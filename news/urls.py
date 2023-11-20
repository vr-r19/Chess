from django.urls import path, include
from dateen.views import CategoryListView, FeaturedArticleListView
urlpatterns = [
    path("",CategoryListView.as_view())
]
