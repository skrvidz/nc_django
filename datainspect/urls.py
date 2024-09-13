from django.urls import path
from . import views  # Ensure that this line is present
from .views import OperationalVariableCreateAPIView, SystemStateCreateAPIView, PerformanceMetricCreateAPIView, LogRecordCreateAPIView, DynamicSystemCreateAPIView, BlockDiagramCreateAPIView, RLTrainedModelCreateAPIView, CSVDataSetCreateAPIView, CSVDataSetListAPIView, DynamicSystemListAPIView
urlpatterns = [
    # Webpage route
    path('', views.index, name='index'),

    # API route for existing data types
    path('api/variables/', OperationalVariableCreateAPIView.as_view(), name='create-variable'),
    path('api/system-states/', SystemStateCreateAPIView.as_view(), name='create-system-state'),
    path('api/performance-metrics/', PerformanceMetricCreateAPIView.as_view(), name='create-performance-metric'),
    path('api/log-records/', LogRecordCreateAPIView.as_view(), name='create-log-record'),

    # API routes for file uploads
    path('api/csv-datasets/', CSVDataSetCreateAPIView.as_view(), name='create-csv-dataset'),
    path('api/dynamic-systems/', DynamicSystemCreateAPIView.as_view(), name='create-dynamic-system'),
    path('api/block-diagrams/', BlockDiagramCreateAPIView.as_view(), name='create-block-diagram'),
    path('api/rl-models/', RLTrainedModelCreateAPIView.as_view(), name='create-rl-trained-model'),
    path('api/csv-datasets-list/', CSVDataSetListAPIView.as_view(), name='list-csv-datasets'),
    path('api/dynamic-systems-list/', DynamicSystemListAPIView.as_view(), name='list-dynamic-systems'),

    # Data table route
    path('variables/', views.operational_variable_table, name='operational_variable_table'),
]