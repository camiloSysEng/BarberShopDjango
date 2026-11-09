from django.shortcuts import render

def agendar(request):
    return render(request, 'citas/agendar.html')