from django.views.generic import CreateView

from core.models import Attraction, Tour, Food, Outdoor, Shopping
from core.mixins import LoginRequiredMixin

class AttractionCreateView(LoginRequiredMixin, CreateView):
    login_url = 'core:user_login'
    fields = ['name', 'short_description', 'long_description', 'address', 'covid_safe', 'type', 'neighborhood', 'good_for']
    model = Attraction
    template_name = 'core/thing_forms/attraction.html'

    # manually setting a "default" category on the form before submitting
    def form_valid(self, form):
        form.instance.category = 'Attraction'
        return super().form_valid(form)

class FoodCreateView(LoginRequiredMixin, CreateView):
    login_url = 'core:user_login'
    fields = ['name', 'short_description', 'long_description', 'address', 'covid_safe', 'type', 'neighborhood', 'good_for']
    model = Food
    template_name = 'core/thing_forms/food.html'

    def form_valid(self, form):
        form.instance.category = 'Food'
        return super().form_valid(form)

class OutdoorCreateView(LoginRequiredMixin, CreateView):
    login_url = 'core:user_login'
    fields = ['name', 'short_description', 'long_description', 'address', 'covid_safe', 'type', 'neighborhood', 'good_for']
    model = Outdoor
    template_name = 'core/thing_forms/outdoor.html'

    def form_valid(self, form):
        form.instance.category = 'Outdoor'
        return super().form_valid(form)

class ShoppingCreateView(LoginRequiredMixin, CreateView):
    login_url = 'core:user_login'
    fields = ['name', 'short_description', 'long_description', 'address', 'covid_safe', 'type', 'neighborhood', 'good_for']
    model = Shopping
    template_name = 'core/thing_forms/shopping.html'

    def form_valid(self, form):
        form.instance.category = 'Shopping'
        return super().form_valid(form)

class TourCreateView(LoginRequiredMixin, CreateView):
    login_url = 'core:user_login'
    fields = ['name', 'short_description', 'long_description', 'address', 'covid_safe', 'type', 'price', 'duration']
    model = Tour
    template_name = 'core/thing_forms/tour.html'

    def form_valid(self, form):
        form.instance.category = 'Tour'
        return super().form_valid(form)
