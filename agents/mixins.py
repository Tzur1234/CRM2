from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class OrganizorAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an organisor."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organizor:
            return redirect("leads:leads")
        return super().dispatch(request, *args, **kwargs)