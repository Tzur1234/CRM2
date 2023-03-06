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
from agents.mixins import OrganizorAndLoginRequiredMixin

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserSignCustomForm 
    
    def get_success_url(self):
        return reverse("login")

class DashboardPageView(LoginRequiredMixin, TemplateView):
    template_name="index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Retrieve all leads
        
        user = self.request.user
        
        if user.is_organizor:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            #  1 - Filter by organization
             queryset = Lead.objects.filter(organization=user.agent.organization)
            # 2  - Filter by agent
             queryset =  queryset.filter(agent__user=user)
        
        context["leads"] = queryset 
        return context
    
class HomePageView(TemplateView):
    template_name="home_page.html"

class LeadListView(LoginRequiredMixin, ListView): 
    template_name = 'lead_list.html'
    context_object_name = 'leads'
    
    # is_orgenizor -> show all the leade form your organization
    # is_agent -> show all lead that relate to you
    def get_queryset(self):
        user = self.request.user
        
        if user.is_organizor:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            #  1 - Filter by organization
             queryset = Lead.objects.filter(organization=user.agent.organization)
            # 2  - Filter by agent
             queryset =  queryset.filter(agent__user=user)
        
        return queryset
     
class LeadCreateView(OrganizorAndLoginRequiredMixin, CreateView):
    template_name = 'lead_create.html'
    model = Lead
    form_class = CreateLeadForm

    def form_valid(self, form):
        # set Lead - Organization !
        lead = form.save(commit=False)
        lead.organization = self.request.user.userprofile
        lead.save()

        send_mail(
            "A new lead has beem created !",
            "Go to the site to see the new lead",
            "test2gmail.com",
            ['test2gmail.com']
        )

        return super(LeadCreateView, self).form_valid(form)

    # return all organzations' leads
    def get_queryset(self):
        queryset = Lead.objects.filter(organization=user.userprofile)
        return queryset
    
    def get_success_url(self):
        return reverse('leads:leads')

class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = 'lead_detail.html'
    model = Lead

    def get_queryset(self):
        user = self.request.user
        
        if user.is_organizor:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            #  1 - Filter by organization
             queryset = Lead.objects.filter(organization=user.agent.organization)
            # 2  - Filter by agent
             queryset =  queryset.filter(agent__user=user)
        
        return queryset
class LeadUpdateView(OrganizorAndLoginRequiredMixin, UpdateView):
    template_name = 'lead_update.html'
    model = Lead
    form_class = CreateLeadForm
    context_object_name = 'lead'

    # return all organzations' leads
    def get_queryset(self):
        queryset = Lead.objects.filter(organization=user.userprofile)
        return queryset
    
    def get_success_url(self):
        return reverse('leads:leads')
  
class LeadDeleteView(OrganizorAndLoginRequiredMixin, DeleteView):

    template_name = "delete_lead.html"
    model= Lead
    context_object_name = 'lead'
    
    # return all organzations' leads
    def get_queryset(self):
        queyset = Lead.objects.filter(organization=user.userprofile)
        return queyset
    
    def get_success_url(self):
        return reverse('leads:leads')   