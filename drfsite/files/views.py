from rest_framework import permissions, viewsets, generics
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Post, Article
from .serializers import PostSerializer, ArticleSerializer

from rest_framework.response import Response


# class MyModelViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.order_by('-creation_date')
#     serializer_class = PostSerializer
#     parser_classes = (MultiPartParser, FormParser)
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(creator=self.request.user)


class ArticleAPIList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    parser_classes = (MultiPartParser, FormParser)
    
    def perform_create(self, serializer):
        img = self.request.data.get('image')
        print(img)
        serializer.save(user=self.request.user)
        
    # def get(self, request, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)
    
    # def get(self, request, *args, **kwargs):
    #     games = Article.objects.all()
    #     return Response({"data": "kek"})
    # permission_classes = (IsAuthenticatedOrReadOnly, )
    # pagination_class = GameAPIListPagination÷
