from django import forms

class PizzaForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    size = forms.ChoiceField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extralarge')], required=True)
    price = forms.DecimalField(max_digits=5, decimal_places=2, required=True)
    date_created = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    image = forms.ImageField(required=False)

    class Meta:
        fields = ['name', 'size', 'price', 'date_created', 'image']
      



