from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),                     # الصفحة الرئيسية
    path('menu/', views.coffee_menu, name='list'),           # صفحة المنيو
    path('menu/<int:coffeeId>/', views.view_coffee, name='details'), # صفحة التفاصيل للقهوة
    path('about/', views.about, name='about'), # صفحة عن متجري المتواضع
    path('desert/', views.desert_menu, name='desert'), # صفحة الحلى
]