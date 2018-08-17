"""tweetme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from accounts.views import UserRegisterView
from hashtags.api.views import TagTweetAPIView
from hashtags.views import HashTagView
from tweets.api.views import SearchTweetAPIView
from tweets.views import TweetListView
from .views import home, SearchView

urlpatterns = [
    path('', TweetListView.as_view(), name="home"),
    path('search/', SearchView.as_view(), name="search"),
    path('admin/', admin.site.urls),
    path('api/tweet/', include('tweets.api.urls')),
    path('api/tags/<slug:hashtag>/',
         TagTweetAPIView.as_view(), name="tag-tweet-api"),
    path('api/search/', SearchTweetAPIView.as_view(), name="search-api"),
    path('api/', include('accounts.api.urls')),
    path('tags/<slug:hashtag>/', HashTagView.as_view(), name="hashtag"),
    path('tweet/', include('tweets.urls')),
    path('register/', UserRegisterView.as_view(), name="register"),
    path('', include('django.contrib.auth.urls')),
    path('', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL,
                           document_root=settings.STATIC_ROOT))
