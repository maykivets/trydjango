from django.shortcuts import render, get_object_or_404

from .forms import ProductForm
from .models import Product
# Create your views here.


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, 'product_create.html', context)


def product_detail_view(request):
    obj = Product.objects.get(id=2)
    context = {
        'title': obj.title,
        'description': obj.description,
    }
    return render(request, 'product/detail.html', context)


def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    context = {
        'title': obj.title,
        'description': obj.description,
    }
    return render(request, 'product/detail.html', context)
