from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404

# Create your views here.
def kush(request):
    chais = ChaiVarity.objects.all()
    return render(request,'kush/kush.html',{'chais': chais})

def chai_detail(request,chai_id):
    chai = get_object_or_404(ChaiVarity,pk=chai_id)
    return render(request,'kush/chai_detail.html',{'chai':chai})


    