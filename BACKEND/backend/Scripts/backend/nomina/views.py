from django.shortcuts import render

from rest_framework import generics
from .models import Empleado
from .serializers import EmpleadoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Sum
class EmpleadoList(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class EmpleadoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class EmpleadoUpdate(generics.UpdateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class EmpleadoDelete(generics.DestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class EmpleadoCreate(generics.CreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
        
@api_view(['GET'])
def informe_nomina(request):
    total_nomina = Empleado.objects.aggregate(total=Sum('salario_base'))['total']
    empleados = Empleado.objects.all().values('nombre', 'salario_base')
    informe = {
        'total_nomina': total_nomina,
        'empleados': empleados
    }
    return Response(informe)