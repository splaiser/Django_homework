from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
import csv
from django.http import HttpResponse
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page', 1))
    with open(BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        CONTENT = [row for row in reader]
        paginator = Paginator(CONTENT, 10)
        page = paginator.get_page(page_number)
        page_for = paginator.page(page_number)
        context = {
                    'bus_stations': page,
                    'page': page_for
                }

    return render(request, 'stations/index.html', context)
