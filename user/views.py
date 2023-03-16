from django.shortcuts import render


def profile(request):
    user = request.user
    return render(request, 'user/profile.html', {'user': user})
