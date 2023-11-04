from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses http method as function get,post,patch,put,delete',
            'Is smilar ta a traditional Django view',
            'Give you the most control over your application'
        ]

        return Response({'message': "Hello", 'an_apiview': an_apiview})
