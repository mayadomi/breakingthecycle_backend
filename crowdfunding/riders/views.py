from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from .models import Rider, Donation, RiderUpdates
from .serializers import RiderSerializer, DonationSerializer, RiderDetailSerializer, RiderUpdateSerializer, RiderDeSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly


class RiderList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        riders = Rider.objects.all()

        serializer = RiderDeSerializer(riders, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = RiderSerializer(data=request.data)
        
        if serializer.is_valid():
            print(self.request.user.id)
            if Rider.objects.filter(rider_owner=self.request.user.id).exists():
                return Response("A rider already exists for this account", status=status.HTTP_400_BAD_REQUEST)
            else:
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

class RiderUpdatesList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            rider = Rider.objects.get(rider_owner=pk)
            return rider
        
        except Rider.DoesNotExist:
            raise Http404
        
    def get(self, request):
        updates = RiderUpdates.objects.all()
        serializer = RiderUpdateSerializer(updates, many=True)
        return Response(serializer.data)
    
    def post(self, request, pk):

        serializer = RiderUpdateSerializer(data=request.data)
        
        rider = self.get_object(pk)

        if serializer.is_valid():
            if  rider.rider_owner.id == self.request.user.id:
                serializer.save(rider_posting=rider)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response("Unauthorized, you must be the rider to post an update", status=status.HTTP_401_UNAUTHORIZED)
            



class DonationList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            donation = Donation.objects.get(pk=pk)
            #self.check_object_permissions(self.request, rider)
            return donation
        except Donation.DoesNotExist:
            raise Http404


    def get(self, request):
        donations = Donation.objects.all()
        serializer = DonationSerializer(donations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DonationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(donor=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        id = self.get_object(pk)

        if id:
            Donation.objects.get(id=pk).delete()
            return Response(status.HTTP_204_NO_CONTENT)
        return Response(status.HTTP_404_NOT_FOUND)


class DonationDeletionView(DestroyAPIView):
    
    queryset = Donation.objects.all()
    serializer = DonationSerializer


