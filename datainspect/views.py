from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import OperationalVariable, SystemState, PerformanceMetric, LogRecord, DynamicSystem, BlockDiagram, RLTrainedModel, CSVDataSet
from .serializers import OperationalVariableSerializer, SystemStateSerializer, PerformanceMetricSerializer, LogRecordSerializer, DynamicSystemSerializer, BlockDiagramSerializer, RLTrainedModelSerializer, CSVDataSetSerializer
import pandas as pd

def index(request):
    return render(request, 'index.html')

class OperationalVariableCreateAPIView(APIView):
    def post(self, request):
        serializer = OperationalVariableSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SystemStateCreateAPIView(APIView):
    def post(self, request):
        serializer = SystemStateSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PerformanceMetricCreateAPIView(APIView):
    def post(self, request):
        serializer = PerformanceMetricSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogRecordCreateAPIView(APIView):
    def post(self, request):
        serializer = LogRecordSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DynamicSystemCreateAPIView(APIView):
    def post(self, request):
        serializer = DynamicSystemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DynamicSystemListAPIView(APIView):
    def get(self, request):
        systems = DynamicSystem.objects.all()
        data = [{'label': system.system_name, 'value': system.json_file.url} for system in systems]
        return Response(data)

class BlockDiagramCreateAPIView(APIView):
    def post(self, request):
        serializer = BlockDiagramSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RLTrainedModelCreateAPIView(APIView):
    def post(self, request):
        serializer = RLTrainedModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CSVDataSetCreateAPIView(APIView):
    def post(self, request):
        serializer = CSVDataSetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CSVDataSetListAPIView(APIView):
    def get(self, request):
        datasets = CSVDataSet.objects.all()  # Fetch all datasets
        data = [{'label': f"{dataset.dataset_name}", 'value': dataset.csv_file.url} for dataset in datasets]
        return Response(data)

def operational_variable_table(request):
    # Query the data
    variables = OperationalVariable.objects.all()

    # Handle filtering based on query parameters
    name_filter = request.GET.get('name')
    if name_filter:
        variables = variables.filter(name__icontains=name_filter)

    start_date = request.GET.get('start')
    end_date = request.GET.get('end')
    if start_date and end_date:
        variables = variables.filter(timestamp__range=[start_date, end_date])

    context = {
        'variables': variables
    }

    return render(request, 'operational_variable_table.html', context)

