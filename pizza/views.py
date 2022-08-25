from django.shortcuts import render
from .forms import PizzaForm


# Create your views here.


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    if request.method == "POST":
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            note = "Thanks for order! Your %s %s and %s pizza is on it's way!" % (filled_form.cleaned_data['size'],
                                                                                  filled_form.cleaned_data['topping1'],
                                                                                  filled_form.cleaned_data['topping2'])
            new_pizza_form = PizzaForm()
            return render(request, 'pizza/order.html', {'pizzaform': new_pizza_form, 'note': note})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform': form})
