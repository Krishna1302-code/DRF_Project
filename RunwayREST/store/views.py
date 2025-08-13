from rest_framework.decorators import api_view  #DRF decorator that turns a normal Django function into an API endpoint
from rest_framework.response import Response #DRF's special response object- returns JSON automatically
from rest_framework import status #HTTP status codes eg-200, 404, 201
from .models import Product
from .serializers import ProductModelSerializer #my serializer




#list
@api_view(['GET'])
def list_product(request):
    product = Product.objects.all()
    serializer = ProductModelSerializer(product,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

#Create 
@api_view(['POST'])
def create_product(request):
    serializer = ProductModelSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#Retrieve
@api_view(['GET'])
def get_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProductModelSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)


#Update/put/patch
@api_view(['PUT'])
def update_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND) 
    serializer = ProductModelSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Delete 
@api_view(['DELETE'])
def delete_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



# List & Create
class ProductListCreateView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductModelSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve, Update, Delete
# class ProductDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             return Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             return None

#     def get(self, request, pk):
#         product = self.get_object(pk)
#         if not product:
#             return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = ProductModelSerializer(product)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         product = self.get_object(pk)
#         if not product:
#             return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = ProductModelSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         product = self.get_object(pk)
#         if not product:
#             return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
