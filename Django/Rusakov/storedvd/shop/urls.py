from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delivery', views.delivery, name='delivery'),
    path('contacts', views.contacts, name='contacts'),
    path('section/<int:id>', views.section, name='section'),
    path('product/<int:pk>', views.ProdactDetailView.as_view(), name='product'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart, name='cart'),
    path('order/', views.order, name='order'),
    path('addorder/', views.addorder, name='addorder'),
    path('orders/', views.orders, name='orders'),
    path('cancelorder/<int:id>/', views.cancelorder, name='cancelorder'),
]
