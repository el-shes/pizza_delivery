from django import forms


class PizzaForm(forms.Form):
    size = forms.ChoiceField(label='Size', choices=[('Small', 'small'), ('Medium', 'medium'), ('Large', 'large')])
    topping1 = forms.CharField(label='Topping 1', max_length=100)
    topping2 = forms.CharField(label='Topping 2', max_length=100)