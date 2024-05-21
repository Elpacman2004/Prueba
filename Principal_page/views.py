from django.shortcuts import render

def Index (request):
    return render(request, 'Index.html')

def handler404(request, exception):
    return render(request, '404.html', status=404)