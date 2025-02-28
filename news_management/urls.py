from django.urls import path

from news_management.views import (
    IndexView,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
    NewspaperListView,
    NewspaperDetailView,
    NewspaperRedactorUpdateView,
    NewspaperCreateView,
    NewspaperUpdateView,
    NewspaperDeleteView,
    RedactorListView,
    RedactorDetailView,
    RedactorRegisterView,
    RedactorCreateView,
    RedactorUpdateView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("register/", RedactorRegisterView.as_view(), name="register"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path(
        "topics/<int:pk>/update/",
        TopicUpdateView.as_view(),
        name="topic-update",
    ),
    path(
        "topics/<int:pk>/delete/",
        TopicDeleteView.as_view(),
        name="topic-delete",
    ),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path(
        "newspapers/<int:pk>/",
        NewspaperDetailView.as_view(),
        name="newspaper-detail",
    ),
    path(
        "newspaper/<int:pk>/redactor/<str:action>/",
        NewspaperRedactorUpdateView.as_view(),
        name="newspaper-redactor-update"
    ),
    path(
        "newspapers/create/",
        NewspaperCreateView.as_view(),
        name="newspaper-create",
    ),
    path(
        "newspapers/<int:pk>/update/",
        NewspaperUpdateView.as_view(),
        name="newspaper-update",
    ),
    path(
        "newspapers/<int:pk>/delete/",
        NewspaperDeleteView.as_view(),
        name="newspaper-delete",
    ),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path(
        "redactors/create/",
        RedactorCreateView.as_view(),
        name="redactor-create",
    ),
    path(
        "redactors/<int:pk>/",
        RedactorDetailView.as_view(),
        name="redactor-detail",
    ),
    path(
        "redactors/<int:pk>/update/",
        RedactorUpdateView.as_view(),
        name="redactor-update",
    ),
]

app_name = "news_management"
