from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Survey
from .models import SurveyResult
from .models import InviteeShip
from .serializers import SurveySerializer
from account.models import User


@api_view(["GET"])
def get_created_surveys_within_bang(request):
    surveys = request.user.own_surveys
    serializer = SurveySerializer(surveys.all())
    return Response(serializer.data)


@api_view(["GET"])
def get_invited_surverys_within_bang(request):
    # TODO: get surveys invited me
    surveys = request.user.own_surveys
    serializer = SurveySerializer(surveys)
    return Response(serializer.data)


# @api_view(["GET"])
# def get_answered_surveys_within_bang(request):
#     pass


@api_view(["POST"])
def create_survey(request):
    data = request.DATA.copy()
    data["owner"] = request.user.pk
    data["bang"] = request.current_bang.pk
    serializer = SurveySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        survey = serializer.object
        for invitee in data['invitee']:
            user = User.objects.get(pk=invitee)
            ship = InviteeShip.objects.create(survey=survey,
                    invitee=user)
            ship.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def update_survey(request):
    pass
