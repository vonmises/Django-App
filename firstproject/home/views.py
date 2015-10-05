from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
              "hello_message": "Hello from Moringa"
    }
    return render(request, 'index.html', context)