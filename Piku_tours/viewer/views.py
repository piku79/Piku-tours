from django.http import HttpResponse
from viewer.models import City, Country, Travel

from django.views.generic import (
  TemplateView, ListView, DetailView,
  CreateView, UpdateView, DeleteView,
  FormView
)

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from viewer.forms import ContactForm
from django.urls import reverse_lazy
from django.core.mail import send_mail


class WelcomeView(TemplateView):
  template_name = 'welcome.html'

class TravelListView(ListView):
  template_name = 'travels.html'
  model = Travel
  context_object_name = 'travels'

class TravelDetailView(PermissionRequiredMixin, DetailView):
  template_name = 'travel_details.html'
  model = Travel
  context_object_name = 'travel'
  permission_required = 'viewer.view_travels'


class CreateTravelView(PermissionRequiredMixin, CreateView):
  template_name = 'create_travels.html'
  model = Travel
  fields = '__all__'
  success_url = reverse_lazy('travels')
  permission_required = 'viewer.create_travels'


class UpdateTravelView(PermissionRequiredMixin, UpdateView):
  template_name = 'update_travels.html'
  model = Travel
  success_url = reverse_lazy('travels')
  fields = '__all__'
  permission_required = 'viewer.change_travels'


class DeleteTravelView(PermissionRequiredMixin, DeleteView):
  template_name = 'delete_travels.html'
  model = Travel
  success_url = reverse_lazy('travels')
  context_object_name = 'travel'
  fields = '__all__'
  permission_required = 'viewer.delete_travels'

class ContactView(FormView):
  template_name = 'contact.html'
  form_class = ContactForm
  success_url = reverse_lazy('travels')

  def form_valid(self, form):
    result = super().form_valid(form)
    cleaned_data = form.cleaned_data
    print(cleaned_data)


    send_mail(
      f'Contact email from{cleaned_data["name"]}',
      cleaned_data['message'] + f'User email: {cleaned_data["email"]}',
      'contact@pikutours.com',
      ['helmet.pikkel@gmail.com'],
      fail_silently=False,


    )

    return render(self.request, 'contact_success.html')