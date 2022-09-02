from django.urls import path
from . import views

app_name = 'pizza'
urlpatterns = [
    path('', views.home, name='home_page'),
    path('pizzas', views.pizzas, name='pizzas'),

    path('order', views.order, name='create_order'),
    path('order/<int:pk>', views.edit_order, name='edit_order'),
]
