from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image

def base(request):
    return render(request,'base.html')

def images(request):
    images=Image.objects.all()
    print(images)
    return render(request,'images.html',{'images':images})

def upload(request):
    if request.method == 'POST':
        imgs = request.FILES.getlist('img')
        print(imgs)
        title = request.POST.get('title')
        description = request.POST.get('description')
        type_image = request.POST.get('type_image')

        for img in imgs:
            print(img)
            Image.objects.create(
                img=img,
                title=title,
                description=description,
                type_image=type_image
            )
        return redirect('images')    
    return render(request, 'upload.html')

def delete(request):
    if request.method == 'POST':
        ids = request.POST.getlist('delete')
        image=Image.objects.filter(id__in=ids)
        image.delete()
    return redirect('images')