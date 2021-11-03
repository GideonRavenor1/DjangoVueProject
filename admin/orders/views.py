import csv
from django.db import connection
from django.http import HttpResponse
from rest_framework.response import Response
from .serializers import OrderSerializer
from rest_framework import generics, mixins, permissions, views
from .models import Order
from users.authentications import JWTAuthentication


class OrderAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, pk=None):
        if pk:
            data = {
                "data": self.retrieve(request, pk).data
            }
            return Response(data)

        return self.list(request)


class ExportAPIView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename=orders.csv"
        orders = Order.objects.all().prefetch_related("order_items")
        writer = csv.writer(response)
        writer.writerow(["ID", "Name", "Email", "Product Title", "Price", "Quantity"])

        for order in orders:

            writer.writerow([order.pk, order.name, order.email, '', '', ''])

            for item in order.order_items.all():
                writer.writerow(['', '', '', item.product_title, item.price, item.quantity])

        return response


class ChartAPIView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT to_char(o.created_at, 'YYYY-mm-dd') AS date, sum(i.quantity * i.price) AS sum
            FROM orders_order AS o 
            JOIN orders_orderitem AS i ON o.id = i.order_id
            GROUP BY date 
            """)
            row = cursor.fetchall()

        data = [{
            "date": result[0],
            "total": result[1]
        } for result in row]

        return Response(data)
