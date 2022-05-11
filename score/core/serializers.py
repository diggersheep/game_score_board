from score.core.models import (Team, Transition)

from rest_framework import serializers


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'color', 'score', 'sub_score')


class TransitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transition
        fields = ("id", "name", "parameter")
