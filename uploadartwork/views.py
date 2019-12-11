from django.shortcuts import render
from .models import ArtWork, Images
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def add_artwork(request):
    if request.method == 'POST':

        #print(request.POST)
        #print(request.FILES)

        title = request.POST['title']
        description = request.POST['description']
        subject = request.POST['subject']
        category = request.POST['category']
        year = request.POST['year']
        width = request.POST['width']
        height = request.POST['height']
        depth = request.POST['depth']
        material = request.POST['material']
        medium = request.POST['medium']
        styles = request.POST['styles']
        medium = request.POST['medium']
        is_framed = request.POST['framed']
        is_copyright = request.POST['copyright']
        is_approved =  False

        artwork = ArtWork()
        artwork.title = title
        artwork.description = description
        artwork.subject = subject
        artwork.category = category
        artwork.year = year
        artwork.width = width
        artwork.height = height
        artwork.depth = depth
        artwork.material = material
        artwork.medium = medium
        artwork.styles = styles

        if is_framed == 'y':
            artwork.is_framed = True
        else:
            artwork.is_framed = False

        if is_copyright == 'y':
            artwork.is_copyright = True
        else:
            artwork.is_copyright = False

        user = request.user
        artwork.owner = user
        artwork.save()

        #artwork.refresh_from_db()
        
        for file in request.FILES.getlist('images'):
            images = Images()
            images.image = file
            images.post = artwork
            images.save()
        
    return render(request, 'uploadartwork/add_new_artwork.html')


#https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html

def view_artwork(request):
    """ Get current user artwork """

    user = request.user
    artwork_list = ArtWork.objects.filter(owner=user).order_by('id')
    paginator = Paginator(artwork_list, 1)
    page = request.GET.get('page', 1)

    try:
        artworks = paginator.page(page)
    except PageNotAnInteger:
        artworks = paginator.page(1)
    except EmptyPage:
        artworks = paginator.page(paginator.num_pages)

    # To do
    # Get images related to work
    # 
    #print(Images.objects.get())
    return render(request, 'uploadartwork/view_artwork.html', { 'artworks': artworks })

