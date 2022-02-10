from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView

from score.core.models import Team


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        n = Team.objects.all().count()
        context.update({
            "team_range": range(n),
            "n": n,
        })
        return context

class ControlsView(TemplateView):
    template_name = "controls.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "teams": Team.objects.all(),
        })
        return context

urlpatterns = [
    path("", Home.as_view()),
    path("controls", ControlsView.as_view()),
    path("admin/", admin.site.urls),
    path("api/", include("score.core.urls")),
]
