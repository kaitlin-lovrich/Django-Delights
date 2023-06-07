from django.urls import path
from . import views

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),
    # List Views
    path('menu/list', views.MenuItemList.as_view(), name='menu-list'),
    path('ingredient/list', views.IngredientList.as_view(), name='ingredient-list'),
    path('purchase/list', views.PurchaseList.as_view(), name='purchase-list'),
    # Create Views
    path('menu/add', views.MenuItemCreate.as_view(), name='add-menu-item'),
    path('ingredient/add', views.IngredientCreate.as_view(), name='add-ingredient'),
    path('recipe-requirement/add', views.RecipeRequirementCreate.as_view(), name='add-recipe-requirement'),
    path('purchase/add', views.PurchaseCreate.as_view(), name='add-purchase'),
    # Update Views
    path('menu/edit/<pk>', views.MenuItemUpdate.as_view(), name='edit-menu-item'),
    path('ingredient/edit/<pk>', views.IngredientUpdate.as_view(), name='edit-ingredient'),
    path('recipe-requirement/edit/<pk>', views.RecipeRequirementUpdate.as_view(), name='edit-recipe-requirement'),
    path('purchase/edit/<pk>', views.PurchaseUpdate.as_view(), name='edit-purchase'),
    # Delete Views
    path('menu/delete/<pk>', views.MenuItemDelete.as_view(), name='delete-menu-item'),
    path('ingredient/delete/<pk>', views.IngredientDelete.as_view(), name='delete-ingredient'),
    path('recipe-requirement/delete/<pk>', views.RecipeRequirementDelete.as_view(), name='delete-recipe-requirement'),
    path('purchase/delete/<pk>', views.PurchaseDelete.as_view(), name='delete-purchase'),
]