from django.core.files.storage import default_storage
from rest_framework import generics, mixins, permissions, views, parsers
from rest_framework.response import Response
from .models import Product
from users.authentications import JWTAuthentication
from .serializers import ProductSerializers


class ProductAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def get(self, request, pk=None):
        if pk:
            data = {
                "data": self.retrieve(request, pk).data
            }
            return Response(data)

        return self.list(request)

    def post(self, request):
        data = {
            "data": self.create(request).data
        }
        return Response(data)

    def put(self, request, pk=None):
        data = {
            "data": self.update(request, pk).data
        }
        return Response(data)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class FileUploadView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (parsers.MultiPartParser,)

    @staticmethod
    def post(request):
        file = request.FILES.get('image')
        file_name = default_storage.save(file.name, file)
        url = default_storage.url(file_name)
        data = {
            "url": 'http://127.0.0.1:8000/api/v1/products' + url
        }
        return Response(data)
