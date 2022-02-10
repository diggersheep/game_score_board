from django.db import models
from django.utils.translation import gettext_lazy as _


class Team(models.Model):
    color: str = models.CharField(_("Color"), max_length=16, blank=False, null=False)
    score: int = models.IntegerField(_("Score"), default=0)
    sub_score: int = models.IntegerField(_("Sub score"), default=0)

    def __str__(self) -> str:
        return f"{self.color} {self.score}::{self.sub_score}"
