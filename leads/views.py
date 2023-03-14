import datetime

import logging

from django.core.mail import send_mail

from django.shortcuts import render

from django.urls import reverse 

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Lead, Agent, Category, FollowUp

from .forms import UserSignCustomForm, CreateLeadForm, AssignLeadForm, CreateCategoryForm, AssignLeadToCategoryForm, CreateFollowUpForm

from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
    View
)

from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixins import OrganizorAndLoginRequiredMixin

from django.views.generic.edit import FormView

from django.contrib import messages

from django.core.exceptions import ValidationError


class Chart(TemplateView):
    template_name='chart-morris.html'

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserSignCustomForm 
    
    def get_success_url(self):
        return reverse("login")

class DashboardPageView(OrganizorAndLoginRequiredMixin, TemplateView):
    template_name="index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Retrieve all leads       
        user = self.request.user
        queryset = Lead.objects.filter(organization=user.userprofile)
        context["all_leads"] = queryset

        # Retrieve all new leads
        user = self.request.user
        queryset = Lead.objects.filter(organization=user.userprofile)
        context["all_leads"] = queryset

        

        if context["all_leads"].all().count()!=0:
            print('!!!!!!!!!!!!!!!!!!')

            # How many was added in the last 30 days
            thirty_days_ago = datetime.date.today() - datetime.timedelta(days=30)
            context['new_leads'] = Lead.objects.filter(date_added__gte=thirty_days_ago)

            context['new_lead_precentage'] = str((context['new_leads'].count()/ (context["all_leads"].count()))*100) 

            # Retrive  converted in last 30 days
            context["converted_leads"] = context["all_leads"].filter(category__name='Converted', converted_date__gte=thirty_days_ago)
            context['converted_leads_precentage'] = str((context['converted_leads'].count()/ (context["all_leads"].count()))*100)


        # Retrieve unassign leads
        unassign_leads = Lead.objects.filter(organization=user.userprofile, agent__isnull=True)
        context["unassign_leads"] = unassign_leads 

        # Date
        context['today'] = datetime.date.today() 



        return context
    
class HomePageView(TemplateView):
    template_name="home_page.html"

class LeadListView(LoginRequiredMixin, ListView): 
    template_name = 'lead_list.html'
    context_object_name = 'leads'
    
    def get_queryset(self):
        user = self.request.user
        
        if user.is_organizor:
            queryset = Lead.objects.filter(organization=user.userprofile, agent__isnull=False)
        else:
            #  1 - Filter by organization
             queryset = Lead.objects.filter(organization=user.agent.organization, agent__isnull=False)
            # 2  - Filter by agent
             queryset =  queryset.filter(agent__user=user)
        # messages.success(self.request, 'You have successfuly created new lead!', extra_tags='primary')
        # logging.warning("My lead list ")
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        # Organizor   
        if user.is_organizor:
            unassign_leads = Lead.objects.filter(organization=user.userprofile, agent__isnull=True)
            context["unassign_leads"] = unassign_leads 
        return context
       
class LeadCreateView(OrganizorAndLoginRequiredMixin, CreateView):
    template_name = 'lead_create.html'
    model = Lead
    form_class = CreateLeadForm

        # Pass the request object to the __init__ Form function
    def get_form_kwargs(self, **kwargs):
        kwargs = super(LeadCreateView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        return kwargs

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

        # showing a message
        messages.success(self.request, 'You have successfuly created new lead!')
         

        return super(LeadCreateView, self).form_valid(form)

    # Only leads form one organization
    def get_queryset(self):
        user = self.request.user
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

    def get_form_kwargs(self, **kwargs):
        kwargs = super(LeadUpdateView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        return kwargs

    # return all organzations' leads
    def get_queryset(self):
        user = self.request.user
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
        user = self.request.user
        queyset = Lead.objects.filter(organization=user.userprofile)
        return queyset
    
    def get_success_url(self):

        return reverse('leads:leads')   

class AssignLeadView(OrganizorAndLoginRequiredMixin, FormView):
    template_name = 'lead_assign.html'
    form_class = AssignLeadForm

    def form_valid(self,form):
        # Retrieve the selected aggent
        agent = form.cleaned_data['agent']

        # Retrieve the lead according to the data from the url
        lead = Lead.objects.get(id=self.kwargs["pk"])

        # assign new agent to the selected lead
        lead.agent = agent
        lead.save()

        return super(AssignLeadView, self).form_valid(form)

    def get_queryset(self):
        user = self.request.user
        queyset = Lead.objects.filter(organization=user.userprofile, agent__isnull=True)
        return queyset

    # Pass the request object to the __init__ Form function
    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignLeadView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        return kwargs

    def get_success_url(self):       
        return reverse('leads:leads')

class CategoryListView(LoginRequiredMixin, ListView):
    template_name = 'lead_category.html'
    context_object_name = 'categories'
    
    # Categories Queryset
    def get_queryset(self):
        user = self.request.user
        
        if user.is_organizor:
            queryset = Category.objects.filter(organization=user.userprofile)
        else:
            #  1 - Filter by organization
             queryset = Category.objects.filter(organization=user.agent.organization)         
        
        # Categories Queryset
        return queryset
    
class SpecificCategoryView(LoginRequiredMixin, ListView):
    template_name = 'lead_specific_category.html'
    model = Lead
    context_object_name = 'leads'

     # Leads Queryset
    def get_queryset(self):
        user = self.request.user
        
        # Filter by organization
        if user.is_organizor:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else: 
             queryset = Lead.objects.filter(organization=user.agent.organization)
             queryset = queryset.filter(agent__user=user)
           
              
        # filter by category id 
        queryset = queryset.filter(category__pk=self.kwargs["pk"])



        #  Leads Queryset
        return queryset
    
    # Categories Queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        
       
        if user.is_organizor:
            categories = Category.objects.filter(organization=user.userprofile)
        else:
            #  1 - Filter by organization
             categories = Category.objects.filter(organization=user.agent.organization)

        # exclude the selected one
        categories = categories.exclude(pk=self.kwargs["pk"])
        # Categories Queryset
        context["categories"] = categories
        context["selected_category_name"] = Category.objects.filter(pk=self.kwargs["pk"]).first().name
        context["selected_category"] = Category.objects.get(pk=self.kwargs["pk"])
        

        return context
    
class CreateCategoryView(OrganizorAndLoginRequiredMixin, CreateView):
    template_name = "lead_category_create.html"
    model = Category
    form_class = CreateCategoryForm

    def form_valid(self, form):

        # Add organization field
        category = form.save(commit=False)
        category.organization = self.request.user.userprofile
        category.save()
    
        return super(CreateCategoryView, self).form_valid(form)
        
    def get_success_url(self):
        return reverse('leads:category-lead')

class UpdateCategoryView(OrganizorAndLoginRequiredMixin, UpdateView):
    template_name = "lead_category_update.html"
    model = Category
    form_class = CreateCategoryForm


    # Category QuerySet
    def get_queryset(self):
        user = self.request.user
        queyset = Category.objects.filter(organization=user.userprofile)
        return queyset
        
    def get_success_url(self):
        return reverse('leads:category-lead')

class DeleteCategoryView(OrganizorAndLoginRequiredMixin, DeleteView):
    model = Category
    template_name = "lead_category_confirm_delete.html"
    context_object_name = 'category'

    # Category QuerySet
    def get_queryset(self):
        user = self.request.user
        queyset = Category.objects.filter(organization=user.userprofile)
        return queyset

    def get_success_url(self):
        return reverse('leads:category-lead')

class AssignLeadToCategory(OrganizorAndLoginRequiredMixin, FormView):
    
    template_name = 'lead_assign_to_category.html'
    form_class = AssignLeadToCategoryForm

     # Pass the request object  
    
    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignLeadToCategory, self).get_form_kwargs(**kwargs)
        category = Category.objects.filter(pk=self.request.GET.get('pk'))
        kwargs.update({
            "request": self.request,
            "category":category
        })
        
        return kwargs

    
    # Update the DB
    def form_valid(self,form):
        # form = form.save(commit=False)
        # Retrieve the selected aggent    
        lead = form.cleaned_data['leads']
        category = form.cleaned_data['categories']
       

        # Check if converted
        converted_category = Category.objects.get(name='Converted')
        if category == converted_category:
            if lead.category != category:
                lead.converted_date = datetime.datetime.now()

        # Assign
        lead.category = category 
        lead.save()

        return super(AssignLeadToCategory, self).form_valid(form) 
    
    def get_success_url(self):       
        return reverse('leads:category-lead')

# the main purpose- to return a json object of all the leads
class LeadJsonView(View):
    def get(self, request, *args, **kwargs):
        qs = list(Lead.objects.all().values())
        # print(qs)
        return  JsonResponse(qs, safe=False)

class CreateFollowUpView(LoginRequiredMixin, CreateView):
    template_name= 'followup_create.html'
    form_class = CreateFollowUpForm

    def form_valid(self, form):
        # add the lead field
        followup = form.save(commit=False)
        lead = Lead.objects.get(pk=self.kwargs['pk'])
        followup.lead = lead
        followup.save()


        return super(CreateFollowUpView, self).form_valid(form)
        
    
    def get_success_url(self):
        return reverse('leads:detail-lead', kwargs={'pk': self.kwargs['pk']})

class UpdateFollowUpView(LoginRequiredMixin, UpdateView):
    template_name= 'followup_update.html'
    form_class = CreateFollowUpForm

    def get_queryset(self):         
        user = self.request.user
        
        if user.is_organizor:
            queryset = Lead.objects.filter(organization=user.userprofile, agent__isnull=False)
        else:
            #  1 - Filter by organization
             queryset = Lead.objects.filter(organization=user.agent.organization, agent__isnull=False)
            # 2  - Filter by agent
             queryset =  queryset.filter(agent__user=user)
    #    3 - Filter By lead field         
        return FollowUp.objects.filter(lead__in=queryset)
    

    def get_success_url(self):
        return reverse('leads:detail-lead', kwargs={'pk': self.kwargs['lead_id']})

class DeleteFollowUpView(LoginRequiredMixin, DeleteView):
    template_name= 'followup_delete_confirm.html'
    context_object_name = 'followup'

    def get_queryset(self):         
        user = self.request.user
        
        if user.is_organizor:
            queryset = Lead.objects.filter(organization=user.userprofile, agent__isnull=False)
        else:
            #  1 - Filter by organization
             queryset = Lead.objects.filter(organization=user.agent.organization, agent__isnull=False)
            # 2  - Filter by agent
             queryset =  queryset.filter(agent__user=user)
    #    3 - Filter By lead field         
        return FollowUp.objects.filter(lead__in=queryset)
    

    def get_success_url(self):
        return reverse('leads:detail-lead', kwargs={'pk': self.kwargs['lead_id']})










