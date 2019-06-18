from django.shortcuts import render
from phones.models import Phone, Apple, Samsung, Xiaomi

def show_catalog(request):
    context = {
        'Phones': Phone.objects.all(),
        'Additional': [
            Apple.objects.first(),
            Samsung.objects.first(),
            Xiaomi.objects.first()
        ]
    }

    return render(
        request,
        'catalog.html',
        context
    )
