from django.urls import path
from .views import HomeView, InfoView, NewsListView
from . import views

app_name = 'crawlingapp'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('crawling/',views.crawling_run,name='crawling'),
    path('info/',InfoView.as_view(),name='info'),
    path('newslist/',NewsListView.as_view(), name='newslist'),
]