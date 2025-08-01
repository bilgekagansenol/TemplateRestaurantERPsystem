from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Table
from .serializers import TableSerializer

# Listeleme (GET)
class TableListAPIView(APIView):
    def get(self, request):
        tables = Table.objects.all()
        serializer = TableSerializer(tables, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Oluşturma (POST)
class TableCreateAPIView(APIView):
    def post(self, request):
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Silme (DELETE)
class TableDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            table = Table.objects.get(pk=pk)
            table.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Table.DoesNotExist:
            return Response({"error": "Masa bulunamadı"}, status=status.HTTP_404_NOT_FOUND)
