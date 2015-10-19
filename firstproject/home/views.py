from django.shortcuts import render
from django.core.mail import send_mail

from .forms import StudentForm, FeedbackForm
from .models import Student


def index(request):
    return render(request, 'home.html')

def register(request):
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

    return render(request, 'register.html', context)

def feedback(request):
    form = FeedbackForm(request.POST or None)

    if form.is_valid():
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        full_name = first_name + ' ' + last_name
        message = form.cleaned_data.get('message')
        formatted_message = 'You have feedback from {} saying "{}".' \
                            .format(full_name, message)
        from_email = form.cleaned_data.get('email')
        send_mail('Feedback', formatted_message, from_email,
                 ['email'], fail_silently=False)

    context = {
              'form': form
    }

    return render(request, 'feedback.html', context)


def students(request):
    search_term = request.GET.get('search', '')
    students = Student.objects.all().order_by('last_name') \
                      .filter(last_name__contains=search_term)
    context = {
              'students': students
    }
    return render(request, 'students.html', context)


def portfolio(request):
    return render(request, 'delani.html')