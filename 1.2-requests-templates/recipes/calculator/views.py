from django.shortcuts import render, reverse
from requests import request
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },

}


def omlet_view(request):
    template_name = 'calculator/index.html'
    item = DATA.get("omlet")
    servings = request.GET.get("servings", '1')
    for keys, values in item.items():
        item[keys] = values * int(servings)

    context = {
        'recipe': item,
    }

    return render(request, template_name, context)


def pasta_view(request):
    template_name = 'calculator/index.html'
    item = DATA.get("pasta")
    servings = request.GET.get("servings", '1')
    for keys, values in item.items():
        item[keys] = values * int(servings)

    context = {
        'recipe': item,
    }

    return render(request, template_name, context)


def buter_view(request):
    template_name = 'calculator/index.html'
    item = DATA.get("buter")
    servings = request.GET.get("servings", '1')
    for keys, values in item.items():
        item[keys] = values * int(servings)

    context = {
        'recipe': item,
    }

    return render(request, template_name, context)


