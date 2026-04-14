from django.shortcuts import render
from .models import Member

def members(request):
    mymembers = Member.objects.all()
    return render(request, 'myfirst.html', {'mymembers': mymembers})
