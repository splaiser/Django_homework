from django.urls import path
from calculator.views import calculator_view




urlpatterns = [
    path('omlet/', calculator_view, name='omlet'),
    path('pasta/', calculator_view, name='pasta'),
    path('buter/', calculator_view, name='buter'),
]
