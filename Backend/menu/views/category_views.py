from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from menu.models import FoodCategory
from menu.serializers import FoodCategorySerializer

class FoodCategoryListAPIView(APIView):
    def get(self, request):
        queryset = FoodCategory.objects.all()
        serializer = FoodCategorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FoodCategoryCreateAPIView(APIView):
    def post(self, request):
        serializer = FoodCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FoodCategoryDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            category = FoodCategory.objects.get(pk=pk)
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except FoodCategory.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        