from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ECommerceApplication
from .serializers import ECommerceApplicationSerializer, ECommerceApplicationStoreSerializer


class SubmitUserInformation(APIView):
    serializer_class = ECommerceApplicationSerializer
    def post(self, request, format=None):
        serializer = ECommerceApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User information has been successfully saved."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubmitStoreInformation(APIView):
    serializer_class = ECommerceApplicationStoreSerializer
    def post(self, request, format=None):
        try:
            application = ECommerceApplication.objects.get(email=request.data.get('email'))
        except ECommerceApplication.DoesNotExist:
            return Response({"message": "User information has not been saved yet. Please save the user information first."},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = ECommerceApplicationStoreSerializer(instance=application, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "E-commerce account information has been successfully registered. Your application is complete."},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
