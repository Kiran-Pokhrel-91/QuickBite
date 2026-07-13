from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import RegisterSerializer,UserSerializer

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        serializer = UserSerializer(request.user)
        return Response(
            {
                'message': 'User fetched successfully',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )


class RegisterView(APIView):

    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "message": "User registered successfully.",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )