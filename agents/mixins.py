from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class OrganizorAndLoginRequiredMixin(SuccessMessageMixin ,AccessMixin):
    """Verify that the current user is authenticated and is an organisor."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organizor:
            
            # Show error message!
            messages.error(self.request, 'You have no permissions!', extra_tags='danger')
           

            return redirect("leads:leads")
        return super().dispatch(request, *args, **kwargs)