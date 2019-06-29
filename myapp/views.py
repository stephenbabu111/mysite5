from django.shortcuts import render
from myapp.models import ip_table

# Create your views here.
def get_ip_view(request):
    ip=request.META.get('REMOTE_ADDR')
    iptable=ip_table()
    iptable.ip=ip
    iptable.save()
    return render(request,'myapp/home.html')