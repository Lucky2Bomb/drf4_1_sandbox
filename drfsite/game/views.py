from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .models import Game, Category
from .serializers import GameSerializer


class GameAPIListPagination(PageNumberPagination):
    page_size =  2
    page_size_query_param = 'page_size'
    max_page_size = 4


class GameAPIList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = GameAPIListPagination


class GameAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticated, )


class GameAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAdminOrReadOnly, )
    
    


# class GameViewSet(viewsets.ModelViewSet):
#     queryset = Game.objects.all()
#     serializer_class = GameSerializer

#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
        
#         if not pk:
#             return Game.objects.all()[:3]
        
#         return Game.objects.filter(pk=pk)

#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         category = Category.objects.get(pk=pk)
#         return Response({'category': category.name})
    


# class GameAPIView(APIView):
#     def get(self, request):
#         games = Game.objects.all()
#         return Response({"data": GameSerializer(games, many=True).data})

#     def post(self, request):
#         serializer = GameSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({"data": serializer.data})

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk")
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})

#         try:
#             instance = Game.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object not exists"})

#         serializer = GameSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({"data": serializer.data})

#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk")
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})

#         try:
#             instance = Game.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object not exists"})

#         instance.delete()

#         return Response({"message": "object was delete"})
