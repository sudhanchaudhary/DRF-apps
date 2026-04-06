from django.shortcuts import render,redirect
from django.contrib import messages
from rest_framework import viewsets

from .forms import InfoForm
from .models import Info
from .serializer import InfoSerializer
# Create your views here.
def home(request):
    form=InfoForm()
    if request.method == "POST":
        form=InfoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Entry Successful!!, Please visit app B to check the data.')
            return redirect('home')
        else:
            form = InfoForm()
    return render(request,'form.html',{'form':form}) 
class InfoApiView(viewsets.ModelViewSet):
    queryset=Info.objects.all()
    serializer_class=InfoSerializer