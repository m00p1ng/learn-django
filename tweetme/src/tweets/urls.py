from django.urls import path
from django.views.generic.base import RedirectView

from .views import (
    RetweetView,
    TweetCreateView,
    TweetDeleteView,
    TweetDetailView,
    TweetListView,
    TweetUpdateView,
)

app_name = "tweet"

urlpatterns = [
    path('', RedirectView.as_view(url="/")),
    path('search/', TweetListView.as_view(), name="list"),
    path('create/', TweetCreateView.as_view(), name="create"),
    path('<int:pk>/', TweetDetailView.as_view(), name="detail"),
    path('<int:pk>/retweet/', RetweetView.as_view(), name="retweet"),
    path('<int:pk>/update/', TweetUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', TweetDeleteView.as_view(), name="delete"),
]
