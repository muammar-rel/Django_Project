from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('login/', views.loginPage, name='login'),
  path('logout/', views.logoutPage, name='logout'),
  path('register/', views.registerPage, name='register'),
  path('profile/', views.profilePage, name='profile'),
  
  
  
  path("",views.store, name="store"),
  path("cart/",views.cart, name="cart"),
  path("view/",views.cart, name="view"),
  path("checkout/",views.checkout, name="checkout"),
  
  path("update_item/",views.updateItem, name="update_item"),
  path("process_order/",views.processOrder, name="process_order"),
]
