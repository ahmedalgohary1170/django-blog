from django.shortcuts import render ,redirect
from .models import Post,Comment
from .forms import PostForm ,CommentForm







def post_list(request):
    date= Post.objects.all()
    context={
        'object_list':date
    }
    return render(request,'posts/post_list.html',context)



def post_detail(request,pk):
    date= Post.objects.get(id=pk)
    coments=Comment.objects.filter(post=date)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.post=date
            myform.save()

    else:
        form=CommentForm()

    context={
        'post':date,
        'coments': coments,
        'form':form,

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
    
    return render(request,'posts/post_form.html',{'form':form})


def edit_post(request,pk):
    post= Post.objects.get(id=pk)
    if request.method == 'POST':
        form =PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('/posts/')
    else:
        form = PostForm(instance=post)
    
    return render(request,'posts/edit.html',{'form':form})


def delete_post(request,pk):
    post= Post.objects.get(id=pk)
    post.delete()
    return redirect('/posts/')

from django.views.generic import ListView , DetailView,UpdateView,CreateView,DeleteView

class PostList(ListView):
    model =Post

class PostDetail(DetailView):
    model = Post


class AddPost(CreateView):
    model= Post
    fields='__all__'
    success_url='/posts/'


class EditPost(UpdateView):
    model= Post
    fields='__all__'
    success_url='/posts/'
    template_name ='posts/edit.html'



class DeletePost(DeleteView):
    model= Post
    success_url='/posts/'