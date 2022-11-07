from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from rest_framework import status

from .permissions import IsAdminPermission
from .serializers import (
    RegistrationSerializer,
    VerifyAccountSerializer,
    UserSerializer,
    MeSerializer)
from users.models import User
from users.utils import send_confirmation_code


class RegistrationAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            send_confirmation_code(**serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        username = request.data.get('username')
        email = request.data.get('email')
        if User.objects.filter(username=username, email=email).exists():
            send_confirmation_code(**data)
            return Response(
                {'message': 'Check your email for confirmation code'},
                status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyAccountAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        serializer = VerifyAccountSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data['username']
            confirmation_code = serializer.data['confirmation_code']
            user = get_object_or_404(User, username=username)
            if user is None:
                return Response(
                    serializer.data, status=status.HTTP_404_NOT_FOUND)

            if user.confirmation_code != confirmation_code:
                return Response(
                    {'message': 'Wrong confirmation code'},
                    status=status.HTTP_400_BAD_REQUEST)

            user.is_verified = True
            user.save()
            token = RefreshToken.for_user(user)
            return Response(
                {'token': str(token.access_token)}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = MeSerializer
    http_method_names = ['get', 'patch']

    def me(self, request):
        data = request.data
        serializer = MeSerializer(request.user, data=data, partial=True)
        if serializer.is_valid():
            if request.method == 'PATCH':
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsAdminPermission)
    pagination_class = PageNumberPagination
    lookup_field = 'username'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
