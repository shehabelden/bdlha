from knox.models import AuthToken
from knox.serializers import UserSerializer
from rest_framework import generics
from rest_framework.response import Response
from auth_app.serilzer import *
from django.contrib.auth.models import User
from auth_app.models import doctor
class LoginView(generics.GenericAPIView):
    serializer_class = LoginUserSerializer
    def post(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            if  request.user[id] in doctor :
              return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token":AuthToken.objects.create(user)[1],
                 "Permission":"doctor"
            })
