from django import forms
from .models import Pizza


class PizzaForm(forms.Form):
    size = forms.ChoiceField(label='Size', choices=[('Small', 'small'), ('Medium', 'medium'), ('Large', 'large')])
    toppings = forms.MultipleChoiceField(choices=[("pep", "peperoni"), ("cheese", "cheese"), ("olives", "olives")],
                                         widget=forms.CheckboxSelectMultiple)

# class PizzaForm(forms.ModelForm):
#     class Meta:
#         model = Pizza
#         fields = ['size', 'topping1', 'topping2']
#         labels = {'topping1': 'Topping 1', 'topping2': 'Topping 2'}

