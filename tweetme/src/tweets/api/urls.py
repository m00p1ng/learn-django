from django.urls import path
from django.views.generic.base import RedirectView

from .views import (
    LikeToggleAPIView,
    RetweetAPIView,
    TweetCreateAPIView,
    TweetListAPIView,
)

app_name = "tweet-api"

urlpatterns = [
    path('', TweetListAPIView.as_view(), name="list"),
    path('create/', TweetCreateAPIView.as_view(), name="create"),
    path('<int:pk>/like', LikeToggleAPIView.as_view(), name="like-toggle"),
    path('<int:pk>/retweet', RetweetAPIView.as_view(), name="retweet"),
]
