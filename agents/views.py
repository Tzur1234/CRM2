from django.core.mail import send_mail

from django.shortcuts import render

from django.urls import reverse

from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView
)

from leads.models import Agent, Lead, UserProfile
# Create your views here.

from . import forms


from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import OrganizorAndLoginRequiredMixin

from .forms import AgentCreateForm

import random

class AgentListView(OrganizorAndLoginRequiredMixin, ListView):
    template_name = 'agent_list.html'
    model = Agent
    context_object_name = 'agents'


    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

class AgentCreateView(OrganizorAndLoginRequiredMixin, CreateView):
    template_name = 'agent_create.html'
    form_class = AgentCreateForm 
    context_object_name = 'agent'

    def form_valid(self, form): 
        user = form.save(commit=False)       
        
        # Set user status
        user.is_organizor = False
        user.is_agent = True
        # set user pass
        user.set_password(f'{random.randint(0,1000)}')
        user.save()
        # create agent object
        agent = Agent.objects.create(user=user, organization=self.request.user.userprofile)
        
    
        # send email 
        send_mail(
            "You have been added as an agent !",
            "Please reset your password in order to start working ",
            "test2gmail.com",
            ['test2gmail.com']
        )


        return super(AgentCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('agents:agent-list')

class AgentDetailView(OrganizorAndLoginRequiredMixin, DetailView):

    template_name = 'agent_detail.html'
    model = Agent
    context_object_name = 'agent'

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

class AgentUpdateView(OrganizorAndLoginRequiredMixin, UpdateView):
    template_name = 'agent_create.html'
    model = Agent
    context_object_name = 'agent'
    form_class = AgentCreateForm

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

    def get_success_url(self):
        return reverse('agents:agent-list')
        
class AgentDeleteView(OrganizorAndLoginRequiredMixin, DeleteView):
    model = Agent
    template_name = 'agent_delete.html'
    context_object_name = 'agent' 

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

    def get_success_url(self):
        return reverse('agents:agent-list')




