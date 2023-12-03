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

class PostListApi(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=Postserializer

class PostDetailApi(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=Postserializer