from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Img_Files
from django.utils import timezone

def gallery_posts(request):
    All_Posts = Post.objects.all()
    return render(request, 'index.html', {'Posts': All_Posts})


def view_album(request, pk):
    album = get_object_or_404(Post, pk=pk)

    return render(request, 'album.html', {'album':album} )


def new_album(request):
    if request.method == "POST":
        new_post = Post.objects.create(
            author = request.POST['author'],
            title = request.POST['title'],
            text = request.POST['text'],
            created_date = timezone.now()
        )

        imagens = request.FILES.getlist('imgs')
        for img in imagens:
            img_file = Img_Files.objects.create(img=img)
            new_post.posted_imgs.add(img_file)
        
        new_post.save()

        return redirect('view_album', pk=new_post.pk)
    
    else:
        return render (request, 'new_album.html')
