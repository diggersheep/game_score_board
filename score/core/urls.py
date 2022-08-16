from django.urls import path

from score.core import views


from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django.conf import settings


urlpatterns = [
    path("team", views.TeamViewList.as_view()),
    path("team/close_set", views.TeamsCloseSet.as_view()),
    path("team/score_leader", views.TeamsLeader.as_view()),

    path("team/<int:pk>", views.TeamViewUpdate.as_view()),
    path("team/<int:pk>/<op>", views.AddSubTeamAPIView.as_view()),

    path("team/reset", views.TeamReset.as_view()),

    path("transition/current", views.GetActiveTransition.as_view()),
    path("transition/<int:pk>/set_active", views.SetActiveTransition.as_view()),
]


if settings.DEBUG:
    schema_view = get_schema_view(
        openapi.Info(
            title="Sport API doc",
            default_version="v1",
            description="Sport API doc",
        ),
        public=True,
    )
    urlpatterns += [
        path(
            "docs/",
            schema_view.with_ui('swagger', cache_timeout=0),
            name="schema-swagger-ui",
        ),
    ]