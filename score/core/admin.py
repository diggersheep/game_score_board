from django.contrib import admin

from score.core.models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass
