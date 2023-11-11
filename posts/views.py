from django.shortcuts import render
from .models import Post








def post_list(request):
    date= Post.objects.all()
    context={
        'ahmed':date
    }
    return render(request,'posts/post_list.html',context)



def post_detail(request):
    pass

