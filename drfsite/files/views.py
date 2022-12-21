from .models import Post
from .serializers import PostSerializer
from rest_framework import permissions, viewsets
from rest_framework.parsers import MultiPartParser, FormParser

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('-creation_date')
    serializer_class = PostSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)