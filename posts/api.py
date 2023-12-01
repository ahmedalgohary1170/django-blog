from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import Postserializer


@api_view(['GET'])
def post_list_api(request):
    post= Post.objects.all()
    date=Postserializer(post,many=True).data
    return Response({'date':date})