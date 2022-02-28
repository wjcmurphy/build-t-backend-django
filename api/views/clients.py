from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Client
from api.serializers import ClientSerializer


class ClientView(APIView):

    def get(self, request, pk=0):
        if pk > 0:
            try:
                client = Client.objects.get(id=pk)
                serializer = ClientSerializer(client)
            except Client.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            clients = Client.objects.all()
            serializer = ClientSerializer(clients, many=True)
            if len(serializer.data) == 0:
                return Response({'message': 'Clients not found'})

        return Response(serializer.data)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            client = Client.objects.get(id=pk)
            serializer = ClientSerializer(client, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            client = Client.objects.get(id=pk)
            client.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
