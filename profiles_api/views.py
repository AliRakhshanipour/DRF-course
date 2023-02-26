from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HelloAPiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns A List Of APIViews Features"""
        an_apiview = [
            'Uses HTTP methods as functions (get , patch , post , put , delete)',
            'Is similar to a traditional Django view',
            'Gives you the most controll over you application logic',
            'Is Mapped Manually To URLs?']
        return Response({'message': 'Hello !', 'an_apiview': an_apiview})
