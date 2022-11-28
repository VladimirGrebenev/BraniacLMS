from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name="main_page"),
    path("news/", views.NewsPageView.as_view(), name="news"),
<<<<<<< HEAD
    path("news/<int:pk>/", views.NewsPageDetailView.as_view(), name="news_detail"),
    path("courses/", views.CoursesListView.as_view(), name="courses"),
    path(
        "courses/<int:pk>/",
        views.CoursesDetailView.as_view(),
        name="courses_detail",
    ),
=======
    path("news/<int:page>/", views.NewsWithPaginatorView.as_view(), name="news_paginator"),
    path("courses/", views.CoursesPageView.as_view(), name="courses"),
>>>>>>> 9044c7d (Lesson 3 (#2))
    path("contacts/", views.ContactsPageView.as_view(), name="contacts"),
    path("doc_site/", views.DocSitePageView.as_view(), name="doc_site"),
    path("login/", views.LoginPageView.as_view(), name="login"),
]
