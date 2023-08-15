# users/views.py

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from .models import CustomUser
from news.models import News
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserUpdateForm

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        form = CustomUserUpdateForm(instance=request.user)
    return render(request, 'registration/edit_profile.html', {'form': form})


@login_required
def profile(request):
    all_users = None
    if request.user.is_superuser:
        all_users = CustomUser.objects.all()
    recent_news = News.objects.filter(author=request.user).order_by('-created_at')[:5]
    return render(request, 'registration/profile.html', {'all_users': all_users, 'recent_news': recent_news})



@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Your account has been deleted. If you want to use our platform again, you will need to register. We are sorry to see you go.')
        return redirect('register')


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Your registration was successful. Please log in now.')
        return response

