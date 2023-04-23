from django.shortcuts import render

def products(request, sector):
    context = {
        'sector': sector
    }
    return render(request, 'products.html', context)



