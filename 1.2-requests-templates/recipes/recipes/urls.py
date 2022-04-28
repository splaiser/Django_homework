from django.urls import path
from calculator.views import omlet_view, pasta_view, buter_view




urlpatterns = [
    path('omlet/', omlet_view, name='omlet'),
    path('pasta/', pasta_view, name='pasta'),
    path('buter/', buter_view, name='buter'),
    # здесь зарегистрируйте вашу view-функцию
]
