from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from Workout.models import Workout


@login_required
def profile(request):
    user = request.user
    users = User.objects.get(username=request.user.username)
    workouts = Workout.objects.filter(user=users)
    return render(request, 'user/profile.html', {'user': user, 'workouts': workouts})


class UpdateProfile(UpdateView):
    template_name = 'user/update_profile.html'
    model = User
    fields = ['email', 'username']
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        user = self.request.user
        return user


