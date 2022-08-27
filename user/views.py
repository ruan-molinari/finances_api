from django.contrib.auth import login

from rest_framework import permissions, generics, mixins
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken

from .serializers import CreateUserSerializer, UserSerializer

class LoginView(KnoxLoginView):
    """
    Overriding default knox LoginView and setting TokenAuthentication as our 
        default authentication method
    Beware that we are setting up this to use TokenAuthentication class only
    For more info check out https://james1345.github.io/django-rest-knox/auth/
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)

class RegisterView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(type(serializer))
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })
    
class UserView(generics.RetrieveAPIView,):
    
    """
    TODO: update and delete endpoits
    """
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
