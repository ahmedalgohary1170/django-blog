from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import Postserializer

# @api_view(['GET'])
# def post_list_api(request):
#     post= Post.objects.all()
#     date=Postserializer(post,many=True).data
#     return Response({'date':date})


# @api_view(['GET'])
# def post_dateil_api(request,id):
#     post= Post.objects.get(id=id)
#     date=Postserializer(post).data
#     return Response({'date':date})



from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class PostListApi(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=Postserializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['title']
    filterset_fields = ['author', 'title']
    ordering_fields = ['publish_date']



class PostDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=Postserializer