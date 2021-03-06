from django.shortcuts import render, redirect
from .models import Photo, Category


def gallery(request):
    category = request.GET.get('category')

    if category is None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)


def view_photo(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {'photo': photo}
    return render(request, 'photos/photo.html', context)


def add_photo(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        uploaded_image = request.FILES.get('images')
        category_id = data['category']

        if category_id != 'none':
            category = Category.objects.get(id=category_id)
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=uploaded_image
        )
        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'photos/add.html', context)
