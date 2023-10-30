from django import forms


class CreateProductForm(forms.Form):
    image = forms.ImageField(required=True)
    title = forms.CharField(max_length=100, min_length=5)
    description = forms.CharField(max_length=300, min_length=10)
    price = forms.IntegerField(min_value=1, max_value=9999999)


class CreateReviewForm(forms.Form):
    text = forms.CharField(max_length=300, min_length=10)