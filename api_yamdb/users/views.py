from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404

from api.serializers import UserSerializer, VerifyAccountSerializer
from .models import User
from .utils import send_confirmation_code


class RegistrationAPI(APIView):

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            # print(serializer.errors)
            serializer.save()
            send_confirmation_code(**serializer.data)
            return Response(
                {'status': 200,
                 'message': 'Check your email for confirmation code',
                 'data': serializer.data, }
            )

        return Response(
            {'status': 400,
             'message': 'Данные не сериализованны',
             'data': serializer.data, }
        )


class VerifyAccountAPI(APIView):

    def post(self, request):
        data = request.data
        serializer = VerifyAccountSerializer(data=data)
        if serializer.is_valid():
            username = serializer.data['username']
            confirmation_code = serializer.data['confirmation_code']
            user = get_object_or_404(User, username=username)
            # user = User.objects.filter(username=username)
            # if not user.exists():
            if not user:
                return Response(
                    {'status': 400,
                     'message': 'Username not exists', }
                )

            # if user[0].confirmation_code != confirmation_code:
            if user.confirmation_code != confirmation_code:
                return Response(
                    {'status': 400,
                     'message': 'Wrong confirmation code', }
                )

            # user[0].is_verified = True
            # user[0].save()
            user.is_verified = True
            user.save()
            token = RefreshToken.for_user(user)

            return Response(
                {'status': 200,
                 'token': str(token.access_token), }
            )
        return Response(
            {'status': 400,
             'message': 'Something went wrong',
             'data': serializer.data, }
        )
