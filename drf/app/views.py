from django.shortcuts import render
from .forms import InfoForm
from .models import Info
# Create your views here.
def home(request):
    form=InfoForm()
    return render(request,'form.html',{'form':form})