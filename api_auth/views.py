from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


class SessionLogin(APIView):
    """Apiview which provides login functionality"""
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'detail': 'Login Successful'}, status=HTTP_200_OK)
        return Response({'detail': 'Invalid Credentials'}, status=HTTP_400_BAD_REQUEST)
