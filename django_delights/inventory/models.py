from django.db import models

# Create your models here.

class MenuItem(models.Model):
    # Represents a menu item from the restaurant
    
    title = models.CharField(max_length=200, unique=True)
    price = models.FloatField(default=0.00)
    
    def get_absolute_url(self):
        return '/menu/list'
    
    def __str__(self):
        return f'{self.title} ${self.price}'

class Ingredient(models.Model):
    # Represents an ingredient in the restaurant's inventory
    
    name = models.CharField(max_length=200, unique=True)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=200)
    unit_price = models.FloatField(default=0)
    
    def get_absolute_url(self):
        return '/ingredient/list'
    
    def __str__(self):
        return f'{self.unit} {self.name}'

class RecipeRequirement(models.Model):
    # Represents an ingredient required for a recipe from the menu
    
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
    
    def get_absolute_url(self):
        return '/menu/list'
    
    def __str__(self):
        return f'{self.menu_item}: {self.ingredient}'

class Purchase(models.Model):
    # Represents the price of a menu item
    
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return '/purchase/list'
    
    def __str__(self):
        return f'{self.menu_item.__str__()} {self.timestamp}'