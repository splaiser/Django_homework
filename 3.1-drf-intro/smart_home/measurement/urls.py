from django.urls import path
from django.views.generic import TemplateView
from measurement.views import SensorView, Sensor2View, Measurements

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', Sensor2View.as_view()),
    path('measurements/', Measurements.as_view()),


]
