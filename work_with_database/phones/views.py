from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    sort = request.GET.get('sort')
    phones = Phone.objects.all()
    if sort == 'name':
        phones = phones.order_by('name')
    elif sort == 'min-price':
        phones = phones.order_by('price')
    elif sort == 'max-price':
        phones = phones.order_by('-price')

    context = {
        'phones': phones
    }
    return render(
        request,
        'catalog.html',
        context
    )


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone
    }
    return render(
        request,
        'product.html',
        context
    )
