from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delivery', views.delivery, name='delivery'),
    path('contacts', views.contacts, name='contacts'),
    path('section/<int:id>', views.section, name='section')
]
