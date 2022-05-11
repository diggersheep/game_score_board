from django.contrib import admin

from score.core.models import Team, Transition


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Transition)
class TransitionAdmin(admin.ModelAdmin):
    pass
