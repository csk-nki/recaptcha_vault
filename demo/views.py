from django.http import HttpResponse

def index(request):
    """ Just demo that we can do something
    """
    return HttpResponse("Hello, world. You're at %s" % request.get_full_path())
