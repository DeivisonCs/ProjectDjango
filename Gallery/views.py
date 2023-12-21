from django.shortcuts import render
from .models import Post, Img_Files

def gallery_posts(request):
    All_Posts = Post.objects.all()
    return render(request, 'index.html', {'Posts': All_Posts})

# def get_img():
#     All_Post = Post.query.all()
#     return All_Post