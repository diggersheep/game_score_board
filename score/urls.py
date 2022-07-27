from django.contrib import admin
from django.urls import path, include

from django.contrib.sessions.models import Session

from django.views.generic import TemplateView

from score.core.models import Team, Transition


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teams = Team.objects.all()
        n = teams.count()
        context.update({
            "team_range": range(n),
            "n": n,
            "teams": teams,
        })
        return context


class ControlsView(TemplateView):
    template_name = "controls.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "teams": Team.objects.all(),
            "transitions": Transition.objects.all(),
        })
        return context


# scoreboard is the root
urlpatterns = [
    path("scoreboard", Home.as_view()),
    path("scoreboard/controls", ControlsView.as_view()),
    path("scoreboard/admin/", admin.site.urls),
    path("scoreboard/api/", include("score.core.urls")),
]

