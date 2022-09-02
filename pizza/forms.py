from django import forms
from .models import Pizza, Size


# class PizzaForm(forms.Form):
#     size = forms.ChoiceField(label='Size', choices=[('Small', 'small'), ('Medium', 'medium'), ('Large', 'large')])
#     toppings = forms.MultipleChoiceField(choices=[("pep", "peperoni"), ("cheese", "cheese"), ("olives", "olives")],
#                                          widget=forms.CheckboxSelectMultiple)

class PizzaForm(forms.ModelForm):

    # size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)
    # image = forms.ImageField()

    class Meta:
        model = Pizza
        fields = ['size', 'topping1', 'topping2']
        labels = {'topping1': 'Topping 1', 'topping2': 'Topping 2'}


class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=8)
