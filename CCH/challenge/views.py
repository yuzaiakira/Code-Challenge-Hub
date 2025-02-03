from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'challenge/home.html'
