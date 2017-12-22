"""Views for Django Imager."""

from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Home view."""

    template_name = "imagersite/home.html"

    def get_context_data(self, **kwargs):
        """."""
        context = super(HomeView, self).get_context_data(**kwargs)
        user = context['view'].request.user
        if user:
            return {"username": user}
        return {}
