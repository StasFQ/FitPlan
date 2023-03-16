from django.shortcuts import render


def home(request):
    return render(request, 'workout/home.html')


def about(request):
    return render(request, 'workout/about.html')


def contact(request):
    return render(request, 'workout/contact.html')


def trainings(request):
    return render(request, 'workout/trainings.html')


def trainers(request):
    return render(request, 'workout/trainers.html')