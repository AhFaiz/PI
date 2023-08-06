from django.shortcuts import render

# Create your views here.
def IndexData(request):

    return render(request,'DATA/DATA.html',)