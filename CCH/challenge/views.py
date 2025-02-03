from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from challenge.forms import QuestionForm 
from challenge.models import Question


class HomeView(LoginRequiredMixin, CreateView):
    template_name = 'challenge/home.html'
    model = Question
    form_class = QuestionForm
    success_url = '/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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

