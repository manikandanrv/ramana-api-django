from xml.dom import registerDOMImplementation
from accommodation.models import Devotee, Room , Request , Checkin
from accommodation.serializers import DevoteeSerializer, RoomSerializer , RequestSerializer, CheckinSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from accommodation.serializers import UserSerializer
from rest_framework import permissions

from accommodation.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Devotee.objects.all()
#     renderer_classes = [renderers.StaticHTMLRenderer]

#     def get(self, request, *args, **kwargs):
#         devotee = self.get_object()
#         return Response(devotee.highlighted)



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'devotees': reverse('devotee-list', request=request, format=format),
        'rooms': reverse('room-list', request=request, format=format),
        'requests': reverse('request-list', request=request, format=format)
    })

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class DevoteeList(generics.ListCreateAPIView):
    queryset = Devotee.objects.all()
    serializer_class = DevoteeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class DevoteeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Devotee.objects.all()
    serializer_class = DevoteeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RequestList(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CheckinList(generics.ListCreateAPIView):
    queryset = Checkin.objects.all()
    serializer_class = CheckinSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CheckinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Checkin.objects.all()
    serializer_class = CheckinSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

