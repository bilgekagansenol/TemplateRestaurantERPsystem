from django.urls import path
from .views.category_views import (
    FoodCategoryListAPIView,
    FoodCategoryCreateAPIView,
    FoodCategoryDeleteAPIView,
)
from .views.food_item_views import (
    FoodItemListAPIView,
    FoodItemCreateAPIView,
    FoodItemDeleteAPIView,
)

urlpatterns = [
    path('categories/', FoodCategoryListAPIView.as_view(), name='category-list'),
    path('categories/create/', FoodCategoryCreateAPIView.as_view(), name='category-create'),
    path('categories/delete/<int:pk>/', FoodCategoryDeleteAPIView.as_view(), name='category-delete'),
     path('foods/', FoodItemListAPIView.as_view(), name='food-list'),
    path('foods/create/', FoodItemCreateAPIView.as_view(), name='food-create'),
    path('foods/delete/<int:pk>/', FoodItemDeleteAPIView.as_view(), name='food-delete'),

]
