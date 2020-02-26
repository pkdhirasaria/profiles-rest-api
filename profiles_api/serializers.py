from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field filed for testing our APIView"""

    name = serializers.CharField(max_length=10)
