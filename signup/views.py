from django.shortcuts import render, redirect
from signup.forms import SubscriberForm
from signup.models import Subscriber, City


# Create your views here.
def home_page(request):
    print(request)
    if request.method == 'POST':
        form = SubscriberForm(data=request.POST)
        if form.is_valid():
            city = City.objects.get(name__exact=request.POST['city'])
            Subscriber.objects.create(
                email=request.POST['email'],
                city=city)
            return redirect('/')
        return render(request, 'home.html', {'form': form})
    return render(request, 'home.html', {'form': SubscriberForm()})
