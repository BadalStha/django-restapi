from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# this means this endpoint only accepts get requests
@api_view(['GET'])
def product_list_api(request):
    # Fetches all products from database
    products = Product.objects.all()

    # many = True means we are passing a list of data
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)