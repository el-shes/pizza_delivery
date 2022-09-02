from django.urls import path
from . import views

app_name = 'pizza'
urlpatterns = [
    path('', views.home, name='home_page'),
    path('order', views.order, name='create_order'),
    path('pizzas', views.pizzas, name='pizzas'),

]
