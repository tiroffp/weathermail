from django.http import HttpResponse


# Create your views here.
def home_page(request):
    return HttpResponse('<html><title> Weather Powered Email </title></html>')
