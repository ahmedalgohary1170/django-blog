from django.shortcuts import render ,redirect
from .models import Post
from .forms import PostForm 







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


def create_post(request):
    if request.method == 'POST':
        form =PostForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('/posts/')
    else:
        form = PostForm()
    
    return render(request,'posts/new.html',{'form':form})


from django.views.generic import ListView , DetailView

class PostList(ListView):
    model =Post

class PostDetail(DetailView):
    model = Post
