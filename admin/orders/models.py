from django.db import models


class Order(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    @property
    def name(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ['-created_at']


class OrderItem(models.Model):
    product_title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s - %s' % (self.product_title, self.quantity)

    class Meta:
        ordering = ['-created_at']