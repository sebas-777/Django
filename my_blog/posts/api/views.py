from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from posts.models import Post 
from posts.api.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly 
from posts.api.permissions import IsAdminOrReadOnly

class PostModelViewSet(ModelViewSet):
    permission_classes  = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

""" class PostViewSet(ViewSet):
    def list(self, request):
       posts = PostSerializer(Post.objects.all(),many=True)
       return Response(status=status.HTTP_200_OK, data=posts.data) 
   
    def retrieve(self, request,pk: int):
        post = PostSerializer(Post.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=post.data)
   
    def create(self, request):
        posts = PostSerializer(data=request.POST)
        posts.is_valid(raise_exception=True)
        posts.save()
        return Response(status=status.HTTP_200_OK, data=posts.data) """
        
  