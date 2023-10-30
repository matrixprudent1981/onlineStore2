from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review
from .forms import CreateProductForm, CreateReviewForm
# Create your views here.


def productListView(request):
    products = Product.objects.all()
    html_name = "products/products.html"
    context = {
        "products": products
    }
    return render(request, html_name, context)


def productDetailView(request, id):
    if request.method == 'GET':
        product = get_object_or_404(Product, id=id)
        html_name = 'products/product_detail.html'
        context = {
            "product": product,
            'form': CreateReviewForm
        }
        return render(request, html_name, context)
    if request.method == 'POST':
        product = get_object_or_404(Product, id=id)
        data = request.POST
        form = CreateReviewForm(data)

        if form.is_valid():
            Review.objects.create(
                product=product,
                text=form.cleaned_data['text']
            )
            return redirect(f'/products/{id}')

        return render(request, 'products/product_detail.html', {'product': product, 'form': form})


def productCreateView(request):
    if request.method == 'GET':
        context = {
            "form": CreateProductForm
        }

        return render(request, 'products/create_product.html', context)
    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = CreateProductForm(data, files)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            Product.objects.create(
                title=cleaned_data['title'],
                description=cleaned_data['description'],
                price=cleaned_data['price'],
                image=cleaned_data['image']
            )
            return redirect('/products/')

        return render(request, 'products/create_product.html', {'form': form})