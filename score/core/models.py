import json
from typing import Any, Dict

from django.db import models
from django.utils.translation import gettext_lazy as _


class Team(models.Model):
    color: str = models.CharField(_("Color"), max_length=16, blank=False, null=False)
    score: int = models.IntegerField(_("Score"), default=0)
    sub_score: int = models.IntegerField(_("Sub score"), default=0)

    def __str__(self) -> str:
        return f"{self.color} {self.score}::{self.sub_score}"


class Transition(models.Model):
    name = models.CharField(_("Name"), max_length=32, blank=False, null=False)
    parameters = models.JSONField(_("Parameters"), blank=False, null=False, default=dict)
    active = models.BooleanField(_("Active"), default=False)

    def __str__(self) -> str:
        return self.name
