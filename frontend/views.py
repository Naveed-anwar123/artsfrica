from django.shortcuts import render
from uploadartwork.models import ArtWork
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    """ Get current user artwork """

    
    artwork_list = ArtWork.objects.filter(is_approved=True).order_by('id')
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
    return render(request, 'frontend/index.html', { 'artworks': artworks })
    
def detail(request, id):
    """ Frontend details view """

    try:
        artwork = ArtWork.objects.filter(id=id).first().post.all()
    except Exception as identifier:
        return render(request, 'uploadartwork/404.html')        
    
    return render(request, 'frontend/detail_view.html', {'artwork':artwork} )