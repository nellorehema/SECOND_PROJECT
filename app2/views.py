from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dhoni(request):
    return HttpResponse('MSD is best finisher')

def virat(request):
    return HttpResponse('VIRAT IS A BEST BATSMAN')
