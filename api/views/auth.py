from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken


class AuthView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'access_token': token.key,
            'token_type': 'token',
        })

    def get(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'Logout successfully'}, status=status.HTTP_200_OK)
