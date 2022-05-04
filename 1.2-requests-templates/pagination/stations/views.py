from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
import csv
from django.http import HttpResponse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        line_count = 0
        rows = []
        for row in reader:
            if line_count == 10:

                context = {
                    'bus_stations': rows,
                    'page': 1
                }
            else:
                line_count += 1
                rows.append(row)
            # return HttpResponse(context.items())
    return render(request, 'stations/index.html', context)
