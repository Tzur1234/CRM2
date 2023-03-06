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

from .forms import AgentCreateForm

class AgentListView(LoginRequiredMixin, ListView):
    template_name = 'agent_list.html'
    model = Agent
    context_object_name = 'agents'


    def get_queryset(self):
        return Agent.objects.all()

class AgentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'agent_create.html'
    form_class = AgentCreateForm 
    context_object_name = 'agent'

    def form_valid(self, form): 
        # Add organization field
        agent = form.save(commit=False)
        agent.organization = self.request.user.userprofile
        agent.save()
    
        
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

class AgentDetailView(LoginRequiredMixin, DetailView):

    template_name = 'agent_detail.html'
    model = Agent
    context_object_name = 'agent'

    def get_queryset(self):
        queryset = Agent.objects.all()
        return queryset

class AgentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'agent_create.html'
    model = Agent
    context_object_name = 'agent'
    form_class = AgentCreateForm

    def get_queryset(self):
        queryset = Agent.objects.all()
        return queryset

    def get_success_url(self):
        return reverse('agents:agent-list')
        
    


class AgentDeleteView(LoginRequiredMixin, DeleteView):
    model = Agent
    template_name = 'agent_delete.html'
    context_object_name = 'agent' 

    def get_queryset(self):
        queryset = Agent.objects.all()
        return queryset

    def get_success_url(self):
        return reverse('agents:agent-list')




