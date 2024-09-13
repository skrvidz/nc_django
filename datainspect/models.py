from django.db import models
from django.core.exceptions import ValidationError

def validate_zip_extension(value):
    if not value.name.endswith('.zip'):
        raise ValidationError("Only ZIP files are allowed.")

def validate_json_extension(value):
    if not value.name.endswith('.json'):
        raise ValidationError("Only JSON files are allowed.")

def validate_csv_extension(value):
    if not value.name.endswith('.csv'):
        raise ValidationError("Only CSV files are allowed.")

class OperationalVariable(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField(default=0.0)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.value} at {self.timestamp}"

class PerformanceMetric(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField(default=0.0)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.value} at {self.timestamp}"

class SystemState(models.Model):
    state = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.state} - {self.timestamp}"

class LogRecord(models.Model):
    message = models.TextField()
    level = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.level}: {self.timestamp}"

class DataRecord(models.Model):
    operational_variable = models.ForeignKey(OperationalVariable, on_delete=models.CASCADE)
    performance_metric = models.ForeignKey(PerformanceMetric, on_delete=models.CASCADE)
    system_state = models.ForeignKey(SystemState, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Record at {self.timestamp}"

class CSVDataSet(models.Model):
    dataset_name = models.CharField(max_length=100)
    csv_file = models.FileField(upload_to='datasets/', validators=[validate_csv_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dataset_name

class DynamicSystem(models.Model):
    system_name = models.CharField(max_length=100)
    json_file = models.FileField(upload_to='dynamic_systems/', validators=[validate_json_extension])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.system_name

class BlockDiagram(models.Model):
    diagram_name = models.CharField(max_length=100)
    json_file = models.FileField(upload_to='block_diagrams/', validators=[validate_json_extension])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.diagram_name

class RLTrainedModel(models.Model):
    model_name = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    zip_file = models.FileField(upload_to='rl_models/', validators=[validate_zip_extension])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.model_name} (v{self.version})"
