
from pages.models import Pages

def get_pages(request):
    pages = Pages.objects.values_list('id', 'title', 'slug')
    return {
        'pages' : pages
    }