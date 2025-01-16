from django.urls import path

from .views import (
    index,
    TopicListView,
    NewspaperListView,
    NewspaperDetailView,
    NewspaperCreateView,
    RedactorListView,
    RedactorDetailView,
    RedactorCreateView,
    TopicCreateView,
)

urlpatterns = [
    path('', index, name='index'),
    path('topics/', TopicListView.as_view(), name='topic-list'),
    path('topics/create/', TopicCreateView.as_view(), name='topic-create'),
    path('newspapers/', NewspaperListView.as_view(), name='newspaper-list'),
    path(
        'newspapers/<int:pk>/',
        NewspaperDetailView.as_view(),
        name='newspaper-detail'
    ),
    path(
        'newspapers/create/',
        NewspaperCreateView.as_view(),
        name='newspaper-create'
    ),
    path('redactors/', RedactorListView.as_view(), name='redactor-list'),
    path('redactors/create/', RedactorCreateView.as_view(), name='redactor-create'),
    path(
        'redactors/<int:pk>/',
        RedactorDetailView.as_view(),
        name='redactor-detail'
    ),
]

app_name = 'news_management'
