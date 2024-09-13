from rest_framework import serializers
from .models import OperationalVariable, SystemState, PerformanceMetric, LogRecord, DynamicSystem, BlockDiagram, RLTrainedModel, CSVDataSet

class OperationalVariableSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationalVariable
        fields = '__all__'

class SystemStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemState
        fields = '__all__'

class PerformanceMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceMetric
        fields = '__all__'

class LogRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogRecord
        fields = '__all__'

class DynamicSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DynamicSystem
        fields = '__all__'

class BlockDiagramSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockDiagram
        fields = '__all__'

class RLTrainedModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RLTrainedModel
        fields = '__all__'

class CSVDataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSVDataSet
        fields = '__all__'