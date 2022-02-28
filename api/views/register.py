from django.db import transaction, IntegrityError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from api.serializers import RegisterSerializer, ClientSerializer, AdminSerializer, VendorSerializer
from cms import settings


class RegisterView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = RegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        client = ClientSerializer(data=data)
        admin = AdminSerializer(data=data)
        vendor = VendorSerializer(data=data)

        try:
            with transaction.atomic():
                user = serializer.save()
                if data['user_type'] == settings.AUTH_USER_TYPE['admin'] and admin.is_valid(raise_exception=True):
                    admin.save(user=user)
                elif data['user_type'] == settings.AUTH_USER_TYPE['client'] and client.is_valid(
                        raise_exception=True):
                    client.save(user=user)
                elif data['user_type'] == settings.AUTH_USER_TYPE['vendor'] and vendor.is_valid(raise_exception=True):
                    vendor.save(user=user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
