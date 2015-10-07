from django.shortcuts import render
from .forms import StudentForm, FeedbackForm

# Create your views here.

def index(request):
    form = StudentForm(request.POST or None)

    context = {
              "form_message": "Register New Student",
              "form": form
    }

    if form.is_valid():
        first_name = form.cleaned_data.get("first_name")

        if first_name == "admin":
            form.first_name = "superuser"

        form.save()

        context = {
                  "form_message": "Student saved",
        }

    return render(request, 'index.html', context)

def feedback(request):
    form = FeedbackForm(request.POST or None)

    if form.is_valid():
        for key, value in form.cleaned_data.items():
            print(key, value)

    context = {
              "form": form
    }

    return render(request, 'feedback.html', context)