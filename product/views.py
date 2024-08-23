from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category , File , Product
from .serializers import CategorySerializer , FileSerializer , ProductSerializer

class ProductListView(APIView):
    def get(self , request ):
        product = Product.objects.all()
        sreializer = ProductSerializer(product , many=True)
        return Response(sreializer.data) 
    