from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response
from users.models import User

class ResgisterView(APIView):
    def post(self,request):
        print('Registrando usuario ...')
        return Response(status=status.HTTP_200_OK, data='TODO OK')