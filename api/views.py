from rest_framework import generics, status, serializers
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import LoginSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            token = serializer.create(serializer.validated_data)
            return Response(token, status=status.HTTP_200_OK)
        except serializers.ValidationError as e:
            error_detail = str(e)
            if "Unable to log in with provided credentials" in error_detail:
                return Response({'detail': 'Unable to log in with provided credentials'}, status=status.HTTP_400_BAD_REQUEST)
            elif "Must include 'username' or 'email'" in error_detail:
                return Response({'detail': "Must include 'username' or 'email'"}, status=status.HTTP_400_BAD_REQUEST)
            elif "Must include 'password'" in error_detail:
                return Response({'detail': 'Must include password'}, status=status.HTTP_400_BAD_REQUEST)
            elif "User is deactivated" in error_detail:
                return Response({'detail': 'User is deactivated'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'detail': f'An unexpected error occurred: {error_detail}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'detail': f'An unexpected error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
