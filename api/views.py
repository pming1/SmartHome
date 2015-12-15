from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from serializers import SwitchSerializer, UserSerializer, GroupSerializer
from rest_framework import viewsets
from rest_framework import generics
from django.contrib.auth.models import User, Group
from models import Switch
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class SwitchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Switch.objects.all().order_by('-created')
    serializer_class = SwitchSerializer


# class HardwareViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Hardware.objects.all().order_by('-created')
#     serializer_class = HardwareSerializer


# class SwitchList(generics.ListCreateAPIView):
#     queryset = Switch.objects.all()
#     serializer_class = SwitchSerializer
#
#
# class SwitchDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Switch.objects.all()
#     serializer_class = SwitchSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['POST'])
def switch_control(request, pk, action):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        switch = Switch.objects.get(pk=pk)
    except Switch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if action == 'open':
        # open the pk switch
        # data = JSONParser().parse({'result': 'success'})
        return JSONResponse({'result': 'success'}, status=201)
    elif action == 'close':
        # close the pk switch
        # data = JSONParser().parse({'result': 'success'})
        return JSONResponse({'result': 'success'}, status=201)




