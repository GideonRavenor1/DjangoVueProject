from django.urls import path
from .views import OrderAPIView, ExportAPIView, ChartAPIView

app_name = "orders"

urlpatterns = [
    path('', OrderAPIView.as_view(), name="orders"),
    path('order/<str:pk>/', OrderAPIView.as_view(), name="order"),
    path('export/', ExportAPIView.as_view(), name="export"),
    path('chart/', ChartAPIView.as_view(), name="chart")
]
