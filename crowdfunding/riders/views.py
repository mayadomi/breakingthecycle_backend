from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Rider, Donation
from .serializers import RiderSerializer, DonationSerializer, RiderDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly


class RiderList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        riders = Rider.objects.all()
        serializer = RiderSerializer(riders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RiderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(rider_owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RiderDetail(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            rider = Rider.objects.get(pk=pk)
            self.check_object_permissions(self.request, rider)
            return rider
        except Rider.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        rider = self.get_object(pk)
        serializer = RiderDetailSerializer(rider)
        return Response(serializer.data)

    def put(self, request, pk):
        rider = self.get_object(pk)
        serializer = RiderDetailSerializer(
            instance=rider,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()

class DonationList(APIView):

    def get(self, request):
        donations = Donation.objects.all()
        serializer = DonationSerializer(donations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DonationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

