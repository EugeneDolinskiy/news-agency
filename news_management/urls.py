from django.urls import path

from .views import (
    index,
    TopicListView,
    NewspaperListView,
)

urlpatterns = [
    path('', index, name='index'),
    path('topics/', TopicListView.as_view(), name='topic-list'),
    path('newspapers/', NewspaperListView.as_view(), name='newspaper-list'),
]

app_name = 'news_management'
