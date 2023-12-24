from django.shortcuts import render, get_object_or_404
from .models import Post, Img_Files

def gallery_posts(request):
    All_Posts = Post.objects.all()
    return render(request, 'index.html', {'Posts': All_Posts})

def view_album(request, pk):
    album = get_object_or_404(Post, pk=pk)
    return render(request, 'album.html', {'album':album} )