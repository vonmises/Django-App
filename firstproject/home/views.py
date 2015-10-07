from django.shortcuts import render
from django.core.mail import send_mail

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
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        full_name = first_name + ' ' + last_name
        message = form.cleaned_data.get('message')
        formatted_message = 'You have feedback from {} saying "{}".'.format(full_name, message)
        from_email = form.cleaned_data.get('email')
        send_mail('Feedback', formatted_message, from_email,
                 ['email'], fail_silently=False)

    context = {
              "form": form
    }

    return render(request, 'feedback.html', context)