from django.shortcuts import render
from .models import MenuItem, Ingredient, RecipeRequirement, Purchase
from .forms import MenuItemForm, IngredientForm, RecipeRequirementForm, PurchaseForm
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def home(request):
    return render(request, 'inventory/home.html')

# MenuItem views
class MenuItemList(ListView):
    model = MenuItem
    template_name = 'inventory/menu.html'
  
class MenuItemCreate(CreateView):
    model = MenuItem
    template_name = 'inventory/add-menu-item.html'
    form_class = MenuItemForm

class MenuItemUpdate(UpdateView):
    model = MenuItem
    template_name = 'inventory/edit-menu-item.html'
    form_class = MenuItemForm
    success_url = '/menu/list'
    
class MenuItemDelete(DeleteView):
    model = MenuItem
    template_name = 'inventory/delete-menu-item.html'
    success_url = '/menu/list'

# Ingredient views
class IngredientList(ListView):
    model = Ingredient
    template_name = 'inventory/ingredients.html'

class IngredientCreate(CreateView):
    model = Ingredient
    template_name = 'inventory/add-ingredient.html'
    form_class = IngredientForm

class IngredientUpdate(UpdateView):
    model = Ingredient
    template_name = 'inventory/edit-ingredient.html'
    form_class = IngredientForm
    success_url = '/ingredient/list'
    
class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = 'inventory/delete-ingredient.html'
    success_url = '/ingredient/list'

# RecipeRequirement views
class RecipeRequirementCreate(CreateView):
    model = RecipeRequirement
    template_name = 'inventory/add-recipe-requirement.html'
    form_class = RecipeRequirementForm
    
class RecipeRequirementUpdate(UpdateView):
    model = RecipeRequirement
    template_name = 'inventory/edit-recipe-requirement.html'
    form_class = RecipeRequirementForm
    success_url = '/menu/list'
    
class RecipeRequirementDelete(DeleteView):
    model = RecipeRequirement
    template_name = 'inventory/delete-recipe-requirement.html'
    success_url = '/menu/list'

# Purchase views
class PurchaseList(ListView):
    model = Purchase
    template_name = 'inventory/purchases.html'
    
class PurchaseCreate(CreateView):
    model = Purchase
    template_name = 'inventory/add-purchase.html'
    form_class = PurchaseForm
    
class PurchaseUpdate(UpdateView):
    model = Purchase
    template_name = 'inventory/edit-purchase.html'
    form_class = PurchaseForm
    success_url = '/purchase/list'
    
class PurchaseDelete(DeleteView):
    model = Purchase
    template_name = 'inventory/delete-purchase.html'
    success_url = '/purchase/list'
