# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer


class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        req = request.data
        Sensor.objects.create(
            name=req['name'],
            description=req['description']
        )
        return Response({'status': 'OK'})

    def patch(request, **kwargs):
        sensor_id = kwargs.get('pk')
        req = request.data
        Sensor.objects.filter(id=sensor_id).update(description=req['description'])
        return Response({'status': 'OK'})


class Sensor2View(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer



class Measurements(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        req = request.data
        Measurement.objects.create(
            sensor_id=req['sensor'],
            temperature=req['temperature']
        )
        return Response({'status': 'OK'})
