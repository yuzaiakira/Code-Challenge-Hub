from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'challenge/home.html'


class LoginView(LoginView):
    template_name = 'challenge/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')

