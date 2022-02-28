from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Vendor
from api.serializers import VendorSerializer


class VendorView(APIView):

    def get(self, request, pk=0):
        if pk > 0:
            try:
                client = Vendor.objects.get(id=pk)
                serializer = VendorSerializer(client)
            except Vendor.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            clients = Vendor.objects.all()
            serializer = VendorSerializer(clients, many=True)
            if len(serializer.data) == 0:
                return Response({'message': 'Clients not found'})

        return Response(serializer.data)

    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            client = Vendor.objects.get(id=pk)
            serializer = VendorSerializer(client, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except Vendor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            client = Vendor.objects.get(id=pk)
            client.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Vendor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
