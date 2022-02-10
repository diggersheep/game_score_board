from rest_framework import generics
from django.views.generic import View
from django.http import JsonResponse, Http404


from score.core.models import Team
from score.core.serializers import TeamSerializer


class TeamViewList(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamViewUpdate(generics.UpdateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class AddSubTeamAPIView(View):
    def get(self, request, **kwargs):
        team_id = self.kwargs["pk"]
        op = self.kwargs["op"]

        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            raise Http404

        match op:
            case "add":
                team.sub_score += 1
            case "sub":
                if team.sub_score > 0:
                    team.sub_score -= 1
            case _:
                raise Http404

        team.save()
        return JsonResponse({
            "score": team.score,
            "sub_score": team.sub_score,
            "id": team.id,
        })


class TeamsCloseSet(View):
    def get(self, request, **kwargs):
        teams = Team.objects.all()
        max_sub_score = max(teams, key=lambda t: t.sub_score).sub_score
        winners = []

        for t in teams:
            if t.sub_score == max_sub_score:
                winners.append(t)

        for t in winners:
            t.score += 1
            t.save()

        teams.update(sub_score=0)

        response = {
            "winners": [t.id for t in winners],
            "teams": [{
                "id": t.id,
                "score": t.score,
                "sub_score": t.sub_score,
            } for t in teams]
        }
        return JsonResponse(response)


class TeamsLeader(View):
    def get(self, request, **kwargs):
        teams = Team.objects.all()

        max_score = max(teams, key=lambda t: t.score).score
        leader_teams = []
        for team in teams:
            if team.score >=max_score:
                leader_teams.append(team)

        response = {
            "leaders": [t.id for t in leader_teams],
        }
        return JsonResponse(response)
