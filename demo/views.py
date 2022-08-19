from django.contrib.auth import login, logout
from knox.views import LoginView as KnoxLoginView
from knox.views import LogoutView as KnoxLogoutView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@permission_classes((AllowAny,))
class LoginView(KnoxLoginView):
    authentication_classes = []

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        knox_response = super(LoginView, self).post(request, format=None)
        knox_response.set_cookie(key='Token', value=knox_response.data.get('token'), httponly=True)
        return knox_response


@permission_classes((AllowAny,))
class LogoutView(KnoxLogoutView):
    authentication_classes = []

    def post(self, request, format=None):
        logout(request)
        response = Response()
        response.delete_cookie(key='Token')
        response.delete_cookie(key='csrftoken')
        return response
