from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.views import APIView 
from .serializer import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()  # ✅ important
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=201)
        return Response(serializer.errors, status=400)

class LoginView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
       username = request.data.get("username")
       password = request.data.get("password")
       user = User.objects.filter(username=username).first() or User.objects.filter(email=username).first()
       if user and user.check_password(password):
              refresh = RefreshToken.for_user(user)
              return Response({
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                })
       else:
              return Response({"error": "Invalid Credentials"}, status=400)
       
class LogoutView(APIView):
     def post(self, request, *args, **kwargs):
          try:
                refresh_token = request.data["refresh"]
                token = RefreshToken(refresh_token)
                token.blacklist()  # add token to blacklist
                return Response({"message": "Logout successful"}, status=200)
          except Exception as e:
                return Response({"error": "Invalid token"}, status=400)