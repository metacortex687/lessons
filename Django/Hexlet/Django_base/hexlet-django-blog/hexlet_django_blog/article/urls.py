from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), #todo добавить articles_
    path('<int:id>/edit/', views.ArticleFormEditView.as_view(), name='articles_update'), #todo article переименовать в articles везде
    path('<int:id>/delete/', views.ArticleFormDeleteView.as_view(), name='articles_delete'),
    path('<int:id>/', views.ArticleView.as_view(), name='article'),
    path('create/', views.ArticleCreateView.as_view(), name='article_create'),
]
