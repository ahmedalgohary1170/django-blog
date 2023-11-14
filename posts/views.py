from django.shortcuts import render
from .models import Post








def post_list(request):
    date= Post.objects.all()
    context={
        'ahmed':date
    }
    return render(request,'posts/post_list.html',context)



def post_detail(request,post_id):
    
    date= Post.objects.get(id=post_id)
    context={
        'post':date
    }
    return render(request,'posts/post_datail.html',context)


from django.views.generic import ListView , DetailView

class PostList(ListView):
    model =Post

class PostDetail(DetailView):
    model = Post
