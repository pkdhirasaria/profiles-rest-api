from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers
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
