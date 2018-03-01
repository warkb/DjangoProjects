from django.shortcuts import render
from .forms import SubscriberForm

# Create your views here.

def landing(request):
    name = "WarKB"
    current_day = "1.2.2018"
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print('Valid!')
        print(request.POST)
        data = form.cleaned_data
        new_form = form.save()
    return render(request, 'landing/landing.html', locals())
