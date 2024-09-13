import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import *
from .models import *

# Get an instance of a logger
logger = logging.getLogger('order_mgmt_app')  # Replace 'myapp' with your app's name

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self, request, *args, **kwargs):
        logger.debug('Received list request for customers')
        response = super().list(request, *args, **kwargs)
        logger.debug('Response data: %s', response.data)
        return response

    def create(self, request, *args, **kwargs):
        logger.debug('Received create request for customer with data: %s', request.data)
        response = super().create(request, *args, **kwargs)
        logger.info('Created customer with ID: %s', response.data.get('id'))
        return response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        logger.debug('Received list request for products')
        response = super().list(request, *args, **kwargs)
        logger.debug('Response data: %s', response.data)
        return response

    def create(self, request, *args, **kwargs):
        logger.debug('Received create request for product with data: %s', request.data)
        response = super().create(request, *args, **kwargs)
        logger.info('Created product with ID: %s', response.data.get('id'))
        return response

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        logger.debug('Received create request for order with data: %s', request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        logger.info('Created order with data: %s', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        logger.debug('Received list request for orders')
        response = super().list(request, *args, **kwargs)
        logger.debug('Response data: %s', response.data)
        return response

    def retrieve(self, request, *args, **kwargs):
        logger.debug('Received retrieve request for order with ID: %s', kwargs.get('pk'))
        response = super().retrieve(request, *args, **kwargs)
        logger.debug('Response data: %s', response.data)
        return response

    def update(self, request, *args, **kwargs):
        logger.debug('Received update request for order with ID: %s and data: %s', kwargs.get('pk'), request.data)
        response = super().update(request, *args, **kwargs)
        logger.info('Updated order with ID: %s', kwargs.get('pk'))
        return response

    def destroy(self, request, *args, **kwargs):
        logger.debug('Received delete request for order with ID: %s', kwargs.get('pk'))
        response = super().destroy(request, *args, **kwargs)
        logger.info('Deleted order with ID: %s', kwargs.get('pk'))
        return response
