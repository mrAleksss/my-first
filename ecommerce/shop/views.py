from django.shortcuts import render


menu = [{'title': "Home", 'url_name': 'home'},
        {'title': "Каталог товарів", 'url_name': 'pricing'},
        {'title': "Контакти", 'url_name': 'contacts'}]


def index(request):
    context = {
        "menu": menu
    }
    return render(request, 'shop/index.html', context)


def pricing(request):
    context = {}
    return render(request, 'shop/pricing.html', context)


def product_cart(request):
    context = {}
    return render(request, 'shop/product_cart.html', context)


def contacts(request):
    context = {}
    return render(request, 'shop/product_cart.html', context)

