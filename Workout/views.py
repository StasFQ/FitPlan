from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from Workout.models import Workout
from user import tasks
from user.forms import ContactUs


def home(request):
    return render(request, 'workout/home.html')


def about(request):
    return render(request, 'workout/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactUs(request.POST)
        if form.is_valid():
            email = request.user.email
            subject = form.cleaned_data['subject']
            text = form.cleaned_data['text']
            tasks.send_email.delay(subject, text, email)
    else:
        form = ContactUs()
    return render(request, 'workout/contact.html', {'form': form})


def trainings(request):
    return render(request, 'workout/trainings.html')


def trainers(request):
    return render(request, 'workout/trainers.html')


class CreateTraining(CreateView):
    template_name = 'workout/add_training.html'
    model = Workout
    fields = ['name', 'description']
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user
