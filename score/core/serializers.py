from score.core.models import Team

from rest_framework import serializers


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'color', 'score', 'sub_score')
