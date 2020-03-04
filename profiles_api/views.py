from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permission

class HelloAPIViews(APIView):
    """Test APIView"""

    serializer_class = serializers.HelloSerializer
    def get(self,request,format=None):
        """Returns a list of APIView Features"""

        an_apiview = [
            'Uses HTTP methods as function (get,post,put,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview': an_apiview })

    def post(self, requset):
        """Create a hello message with our name """

        serializer = self.serializer_class(data=requset.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                    serializer.errors,
                    status = status.HTTP_400_BAD_REQUEST
                )

    def put(self, pk=None):
        """Handle Updating an object"""

        return Response({'methods':'PUT'})

    def patch(self, pk = None):
        """Handles a partial update of an object"""

        return Response({'methods':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an Object"""

        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API View Sets"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses Action (list,Create,retrive,update,partial_update)',
            'Automatically maps to URLs using Routers',
            'Provide more functionality with less code'
        ]

        return Response({'message':'Hello!', 'a_viewset': a_viewset})

    def create(self,request):
        """Create a new hello message"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrive(self,request,pk=None):
        """Handle getting object by it's ID"""

        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handle Updating an Object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handle updating part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handle Removing an object"""
        return Response({'http_method':'DELETe'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle Creating and Updating profiles"""

    serializer_class = serializers.UserProfileSearializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permission.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email')

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
