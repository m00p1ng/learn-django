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

from hashtags.views import HashTagView
from tweets.views import TweetListView
from .views import home

urlpatterns = [
    path('', TweetListView.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('api/tweet/', include('tweets.api.urls')),
    path('api/', include('accounts.api.urls')),
    path('tags/<slug:hashtag>/', HashTagView.as_view(), name="hashtag"),
    path('tweet/', include('tweets.urls')),
    path('', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL,
                           document_root=settings.STATIC_ROOT))
