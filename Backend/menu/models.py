from django.db import models

class FoodCategory(models.Model):
    '''Model representing a category of food items. Each category can have multiple food items associated with it.'''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    '''Model representing a food item. Each food item can belong to a category and has attributes like name, description, price, and availability.'''
    category = models.ForeignKey(FoodCategory, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_food = models.ImageField(upload_to='food_images/', blank=True, null=True)


    def __str__(self):
        return self.name
