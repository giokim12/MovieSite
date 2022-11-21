# authentication > api > views.py
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .renderers import UserJSONRenderer
from .serializers import RegistrationSerializer, UserSerializer
from rest_framework.decorators import api_view
from .models import User
from django.shortcuts import get_object_or_404
# Create your views here.


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    renderer_classes = (UserJSONRenderer, )

    def post(self, request):
        user = request.data

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_user(request, id):
    if request.method == 'GET':
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(user)
        # print(serializer.data)
        return Response(serializer.data)
        # class LoginAPIView(APIView):
        #     permission_classes = (AllowAny,)
        #     renderer_classes = (UserJSONRenderer,)
        #     serializer_class = LoginSerializer

        #     # 1.
        #     def post(self, request):
        #         # 2.
        #         user = request.data

        #         # 3.
        #         serializer = self.serializer_class(data=user)
        #         serializer.is_valid(raise_exception=True)

        #         # 4.
        #         return Response(serializer.data, status=status.HTTP_200_OK)
