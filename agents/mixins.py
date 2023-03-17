from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class OrganizorAndLoginRequiredMixin(SuccessMessageMixin ,AccessMixin):
    """Verify that the current user is authenticated and is an organisor."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organizor:
            
            # Show error message!
            messages.error(self.request, 'You have no permissions to access this page!')
            messages.info(self.request, 'You have been redirected to leads page!')
           

            return redirect("leads:leads")
        return super().dispatch(request, *args, **kwargs)