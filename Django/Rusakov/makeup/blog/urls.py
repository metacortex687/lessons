from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('articles/', views.articles, name='articles'),
    path('archive/<int:year>/<int:month>', views.archive, name='archive'),
    path('single/<int:pk>/', views.SingleArticleView.as_view(), name='single'),
    path('search/', views.search, name='search'),    
]
