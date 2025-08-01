from django.urls import path
from .views import (
    TableListAPIView,
    TableCreateAPIView,
    TableDeleteAPIView,
)

urlpatterns = [
    path('', TableListAPIView.as_view(), name='table-list'),
    path('create/', TableCreateAPIView.as_view(), name='table-create'),
    path('delete/<int:pk>/', TableDeleteAPIView.as_view(), name='table-delete'),
]
