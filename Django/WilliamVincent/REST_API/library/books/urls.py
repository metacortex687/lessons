from django.urls import path
from .views import BoolListView

urlpatterns = [
    path('', BoolListView.as_view(), name='home'),
]
