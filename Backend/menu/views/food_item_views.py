from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from menu.models import FoodItem
from menu.serializers import FoodItemSerializer

class FoodItemListAPIView(APIView):
    def get(self, request):
        queryset = FoodItem.objects.filter(is_available=True)
        serializer = FoodItemSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class FoodItemCreateAPIView(APIView):
    def post(self, request):
        serializer = FoodItemSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FoodItemDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            food = FoodItem.objects.get(pk=pk)
            food.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except FoodItem.DoesNotExist:
            return Response({"error": "Food item not found"}, status=status.HTTP_404_NOT_FOUND)
