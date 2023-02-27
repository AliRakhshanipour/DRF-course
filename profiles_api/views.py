from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api.serializers import HelloSerializer
# Create your views here.


class HelloAPiView(APIView):
    """Test API View"""
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """Returns A List Of APIViews Features"""
        an_apiview = [
            'Uses HTTP methods as functions (get , patch , post , put , delete)',
            'Is similar to a traditional Django view',
            'Gives you the most controll over you application logic',
            'Is Mapped Manually To URLs?']
        return Response({'message': 'Hello !', 'an_apiview': an_apiview})

    def post(self, request):
        """test post method"""

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data)

    def put(self, request, pk=None):
        """test put method"""
        return Response({"method": "put"})

    def patch(self, request, pk=None):
        """test patch method"""
        return Response({"method": "patch"})

    def delete(self, request, pk=None):
        """test delete method"""
        return Response({"method": "delete"})
