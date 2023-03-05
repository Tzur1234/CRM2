from django.core.mail import send_mail

from django.shortcuts import render

from django.urls import reverse 

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Lead

from .forms import UserSignCustomForm, CreateLeadForm

from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView
)
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserSignCustomForm 
    
    def get_success_url(self):
        return reverse("login")

class DashboardPageView(LoginRequiredMixin, TemplateView):
    template_name="index.html"

class HomePageView(TemplateView):
    template_name="home_page.html"

class LeadListView(LoginRequiredMixin, ListView): 
    template_name = 'lead_list.html'
    context_object_name = 'leads'
    
    def get_queryset(self):
        queryset = Lead.objects.all()
        return queryset
     
class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = 'lead_create.html'
    model = Lead
    form_class = CreateLeadForm

    def form_valid(self, form):

        send_mail(
            "A new lead has beem created !",
            "Go to the site to see the new lead",
            "test2gmail.com",
            ['test2gmail.com']
        )

        return super(LeadCreateView, self).form_valid(form)


    def get_queryset(self):
        queryset = Lead.objects.all()
        return queryset
    
    def get_success_url(self):
        return reverse('leads:leads')

class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = 'lead_detail.html'
    model = Lead

    def get_queryset(self):
        queryset = Lead.objects.all()
        return queryset
    

class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'lead_update.html'
    model = Lead
    form_class = CreateLeadForm
    context_object_name = 'lead'

    def get_queryset(self):
        queryset = Lead.objects.all()
        return queryset
    
    def get_success_url(self):
        return reverse('leads:leads')

    
class LeadDeleteView(LoginRequiredMixin, DeleteView):

    template_name = "delete_lead.html"
    model= Lead
    context_object_name = 'lead'
    
    def get_queryset(self):
        queyset = Lead.objects.all()
        return queyset
    

    def get_success_url(self):
        return reverse('leads:leads')   