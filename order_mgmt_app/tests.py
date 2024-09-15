from django.test import TestCase
from .models import *

class CustomerModelTest(TestCase):

    def setUp(self):

        self.customer = Customer.objects.create(name='john doe',
                                                email='abc@gmail.com',
                                                address='123 street')


    def test_customer_creation(self):
        self.assertEqual(self.customer.name, "john doe")
        self.assertEqual(self.customer.email, 'abc@gmail.com')


class ProductModelTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(name="Test Product", price=100.00, qty_available=10)

    def test_product_creation(self):

        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.price, 100.00)
        self.assertEqual(self.product.qty_available, 10)


class OrderModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(name="John Doe", email="john@example.com", address="123 Main St")
        self.product1 = Product.objects.create(name="Test Product 1", price=100.00, qty_available=10)
        self.product2 = Product.objects.create(name="Test Product 2", price=200.00, qty_available=5)
        self.order = Order.objects.create(customer=self.customer)

        # Add order items
        self.order_item1 = OrderItem.objects.create(order=self.order, product=self.product1, quantity=2)
        self.order_item2 = OrderItem.objects.create(order=self.order, product=self.product2, quantity=1)

    def test_order_total_calculation(self):
        self.order.calculate_total()
        self.assertEqual(self.order.total_price, 400.00)  # 2*100 + 1*200 = 400


    def test_product_quantity_update(self):
        self.assertEqual(self.product1.qty_available,8)
        self.assertEqual(self.product2.qty_available,4)

    def test_quantity_exceeding_stock(self):

        with self.assertRaises(ValueError):
            OrderItem.objects.create(order=self.order, product=self.product1, quantity=20)




# from unittest.mock import patch
#
# @patch('order_mgmt_app.models.Product.save', return_value=None)
# def test_product_save(self, mock_save):
#     print('ddddddddddddddddddddddd')
#     product = Product(name='Test',price=100)
#     product.save()
#     mock_save.assert_called_once()