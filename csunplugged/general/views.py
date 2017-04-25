"""Views for the general application."""

from django.views.generic import TemplateView
from django.http import HttpResponse


class GeneralIndexView(TemplateView):
    """View for the homepage that renders from a template."""

    template_name = 'general/index.html'


class GeneralAboutView(TemplateView):
    """View for the about page that renders from a template."""

    template_name = 'general/about.html'


def health_check(request):
    """Return heath check response for Google App Engine.

    Returns a 200 HTTP response for Google App Engine to detect the system
    is running.
    """
    return HttpResponse(status=200)
