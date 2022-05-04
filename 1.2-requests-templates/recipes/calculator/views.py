from django.shortcuts import render, reverse

from django.http import HttpResponse
import json

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


def calculator_view(request):
    template_name = 'calculator/index.html'
    name = request.path
    item = DATA.get(name.replace("/", ""))
    servings = request.GET.get("servings", '1')
    for keys, values in item.items():
        item[keys] = values * int(servings)

    context = {
        'recipe': item,
    }

    return render(request, template_name, context)




