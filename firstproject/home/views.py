from django.shortcuts import render
from .forms import StudentForm

# Create your views here.

def index(request):
    form = StudentForm(request.POST or None)

    context = {
              "hello_message": "Hello from Moringa",
              "form": form
    }

    if form.is_valid():
        form.save()
        context = {
                  "hello_message": "Student saved",
        }

    return render(request, 'index.html', context)