from django.shortcuts import render, redirect
from .models import ArtWork, Images
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, permission_required

@login_required(login_url='/accounts/signin')
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
@login_required(login_url='/accounts/signin')
def view_artwork(request):
    """ Get current user artwork """

    user = request.user
    artwork_list = ArtWork.objects.filter(owner=user).order_by('id')
   
    paginator = Paginator(artwork_list, 12)
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
    images = []
    for art in artwork_list:
        images.append(Images.objects.filter(post=art).last())

    
    obj = zip(artworks,images)
    obj1 = artworks
    
    return render(request, 'uploadartwork/view_artwork.html', { 'artworks': obj , 'art':obj1  })

@permission_required('is_superuser',login_url='/accounts/unauthorized')  
def collection_view(request):
    """ Show all artwork to SuperUser """

    user = request.user
    artwork_list = ArtWork.objects.filter(is_approved=False).order_by('id')
    paginator = Paginator(artwork_list, 12)
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
    images = []
    for art in artwork_list:
        images.append(Images.objects.filter(post=art).last())

    
    obj = zip(artworks,images)
    obj1 = artworks
    
    return render(request, 'uploadartwork/collections.html', { 'artworks': obj , 'art':obj1  })

@permission_required('is_superuser',login_url='/accounts/unauthorized')  
def change_status_view(request):
    """ Approve an artwork """
    
    if request.method == 'POST':
        ids_list = request.POST.getlist('id')
        approved_list = request.POST.getlist('approve')

        intersection = set(ids_list).intersection(approved_list)
        for index in intersection:
            ArtWork.objects.filter(id=index).update(is_approved=True)
    
    return redirect('collection_view')

@permission_required('is_superuser',login_url='/accounts/unauthorized')  
def approved_view(request):
    """ Show Only approved artwork to SuperUser """

    user = request.user
    artwork_list = ArtWork.objects.filter(is_approved=True).order_by('id')
    paginator = Paginator(artwork_list, 12)
    page = request.GET.get('page', 1)

    try:
        artworks = paginator.page(page)
    except PageNotAnInteger:
        artworks = paginator.page(1)
    except EmptyPage:
        artworks = paginator.page(paginator.num_pages)

    images = []
    for art in artwork_list:
        images.append(Images.objects.filter(post=art).last())

    
    obj = zip(artworks,images)
    obj1 = artworks
    
    return render(request, 'uploadartwork/approved.html', { 'artworks': obj , 'art':obj1  })

@permission_required('is_superuser',login_url='/accounts/unauthorized')  
def change_approved_status_view(request):
    """ Approve an artwork """
    
    if request.method == 'POST':
        ids_list = request.POST.getlist('id')
        approved_list = request.POST.getlist('approve')

        intersection = set(ids_list).intersection(approved_list)
        for index in intersection:
            ArtWork.objects.filter(id=index).update(is_approved=False)

    return redirect('approved_view')


def detail_view(request, id):
    """ Detail view of single artwork """

    # To get object
    #artwork = ArtWork.objects.filter(id=id).first()
    #print(artwork)

    # To get query set
    #artwork = ArtWork.objects.filter(id=id)
    #print(artwork)

    try:
        artwork = ArtWork.objects.filter(id=id).first().post.all()
    except Exception as identifier:
        return render(request, 'uploadartwork/404.html')        
    
    return render(request, 'uploadartwork/detail_view.html', {'artwork':artwork} )

@login_required(login_url='/accounts/signin')
def edit_view(request,id):
    """ Edit view for single Artwork """

    artwork = ArtWork.objects.filter(id=id).first()
    if not artwork:
        return render(request, 'uploadartwork/404.html')        
    return render(request, 'uploadartwork/edit_view.html', {'artwork':artwork} )

@login_required(login_url='/accounts/signin')
def update_artwork(request , id):
    """ Update view """

    if request.method == 'POST':
        artwork = ArtWork.objects.filter(id=id).first()
        
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

        artwork.save()
        for file in request.FILES.getlist('images'):
            if file:
                images = Images()
                images.image = file
                images.post = artwork
                images.save()
        return redirect('edit_view',id = request.POST['id'])    

    
