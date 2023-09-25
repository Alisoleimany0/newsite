from django.urls import path
from .views import (ArticleDeleteView ,
ArticleUpdateView , ArticlecreateView)
from . import views

urlpatterns = [
    # path('',ArticleListView.as_view(),name='article_list'),
    path("edit/<int:pk>/",ArticleUpdateView.as_view(),name="article_update"),
    # path("<int:pk>/",ArticleDetailView.as_view(),name="article_detail"),
    path("new/", ArticlecreateView.as_view(),name="article_create"),
    path("delete/<int:pk>/",ArticleDeleteView.as_view(),name="article_delete"),





    path("<int:pk>/",views.article_detail,name="article_detail"),
    path('',views.article_list,name='article_list'),
]

