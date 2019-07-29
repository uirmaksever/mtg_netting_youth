from django.shortcuts import render
from .models import *
#
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.views.generic import CreateView, UpdateView, DetailView, ListView

# Create your views here.

@login_required
@transaction.atomic
def create_profile(request):
    user_form = UserForm()
    profile_form = ProfileForm()
    print(user_form, profile_form)

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # profile_form.fields['user'] = user_form.instance
            profile = profile_form.save(commit=False)
            profile.user = user
            # print(profile_form.user)
            profile.save()


            print("you are at valid post")

            messages.add_message(request, messages.SUCCESS, "User created successfully")
            return redirect('/')
        else:
            print("you are at error post")

            messages.add_message(request, messages.ERROR, "Please correct the error below.")

    return render(request, 'netting_youth/users/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def update_profile(request):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        print(user_form, profile_form)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.add_message(messages.SUCCESS, "User updated successfully.")
            print("you are at valid post")
            return redirect('')
        else:
            messages.add_message(messages.ERROR, "Please correct the error below.")
            print("you are at error post")

    return render(request, 'netting_youth/users/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

class ProblemDetail(DetailView):
    model = Problem
    template_name = 'netting_youth/problem/problem_detail.html'

class ProblemList(ListView):
    model = Problem
    template_name = 'netting_youth/problem/problem_list.html'

def problem_vote_up(request, pk):
    problem = Problem.objects.get(pk=pk)
    problem.votes.up(request.user.pk)
    return redirect('problem-detail', pk=pk)

class FollowedProblemList(ListView):
    model = Problem
    template_name = 'netting_youth/problem/problem_list.html'

    def get_queryset(self):
        return Problem.votes.all(self.request.user.pk)
