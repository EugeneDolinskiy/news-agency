from django.urls import path

from .views import (
    index,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    NewspaperListView,
    NewspaperDetailView,
    NewspaperCreateView,
    NewspaperUpdateView,
    RedactorListView,
    RedactorDetailView,
    RedactorCreateView,
    RedactorUpdateView,
)

urlpatterns = [
    path('', index, name='index'),
    path('topics/', TopicListView.as_view(), name='topic-list'),
    path('topics/create/', TopicCreateView.as_view(), name='topic-create'),
    path(
        'topics/<int:pk>/update/',
        TopicUpdateView.as_view(),
        name='topic-update'
    ),
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
    path(
        'newspapers/<int:pk>/update/',
        NewspaperUpdateView.as_view(),
        name='newspaper-update'
    ),
    path('redactors/', RedactorListView.as_view(), name='redactor-list'),
    path(
        'redactors/create/',
        RedactorCreateView.as_view(),
        name='redactor-create'
    ),
    path(
        'redactors/<int:pk>/',
        RedactorDetailView.as_view(),
        name='redactor-detail'
    ),
    path(
        'redactors/<int:pk>/update/',
        RedactorUpdateView.as_view(),
        name='redactor-update'
    ),
]

app_name = 'news_management'
