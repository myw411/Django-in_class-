# from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# 요 class들은 CVB현식으로 사용할 때
class PostList(ListView):
    model = Post
    template_name = 'blog/index.html' # 요거를 붙여줘야 이 주소를 잡아서 들어감
    ordering = '-pk'                  # 최신순부터 나오게 하도록 
    
class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# # 요거는 FBV 사용할 때 사용
 # # Create your views here.
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
    
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts': posts,
#         }
#     )

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
    
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post':post,
#         }
#     )
