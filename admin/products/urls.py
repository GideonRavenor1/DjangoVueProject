from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    ProductAPIView, FileUploadView
)


app_name = "products"

urlpatterns = [
    path('', ProductAPIView.as_view(), name="products"),
    path('product/<str:pk>/', ProductAPIView.as_view(), name="product"),
    path('upload/', FileUploadView.as_view(), name="upload_file")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
