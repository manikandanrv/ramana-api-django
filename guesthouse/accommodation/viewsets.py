from xml.dom import registerDOMImplementation
from accommodation.models import Devotee, Room , Request , Checkin
from accommodation.serializers import DevoteeSerializer, RoomSerializer , RequestSerializer, CheckinSerializer
from rest_framework import viewsets
from rest_framework.decorators import action

from django.contrib.auth.models import User
from accommodation.serializers import UserSerializer
from rest_framework import permissions
#from accommodation.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status

##Viewsets
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class DevoteeViewSet(viewsets.ModelViewSet):
    queryset = Devotee.objects.all()
    serializer_class = DevoteeSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CheckinViewSet(viewsets.ModelViewSet):
    queryset = Checkin.objects.all()
    serializer_class = CheckinSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    #@detail_route(methods=['put']) # use this for DRF 3.7
    @action(detail=True, methods=['put'])
    def status(self, request, pk):
        obj = self.get_object()
        changed_status = obj.change_status()
        return Response({'success':True, "status_changed": changed_status},status=status.HTTP_200_OK) 

    def checkout(self, request, pk):
        checkin = self.get_object()
        serializer = CheckinSerializer(data=request.data)
        if serializer.is_valid():
            checkout_status = checkin.checkout()
            #checkin.save()
            return Response({'success':True, "checkout": checkout_status},status=status.HTTP_200_OK) 
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

