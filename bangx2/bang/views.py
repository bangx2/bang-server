from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Bang
from .serializers import BangSerializer
from account.serializers import UserSerializer


# from rest_framework import generics
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework import permissions

# class BangList(generics.ListCreateAPIView):
#     queryset = Bang.objects.all()
#     serializer_class = BangSerializer
# 
# 
# class BangDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Bang.objects.all()
#     serializer_class = BangSerializer


@api_view(['GET'])
def get_my_bangs(request):
    bangs = request.user.bangs.all()
    serializer = BangSerializer(bangs)
    return Response(serializer.data)


@api_view(['POST'])
def create_bang(request):
    data = request.DATA.copy()
    data['members'] = request.user.pk
    data['owner'] = request.user.pk
    serializer = BangSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def quit_bang(request, bang_id):
    bang = Bang.objects.get(pk=bang_id)
    bang.members.remove(request.user)
    return Response('%s quit of %s' % (request.user.username, bang.name),\
            status=status.HTTP_200_OK)
    

@api_view(['GET'])
def get_bang_detail(request, bang_id):
    bang = Bang.objects.get(pk=bang_id)
    serializer = BangSerializer(bang)
    return Response(serializer.data)


@api_view(['GET'])
def get_bang_members(request, bang_id):
    bang = Bang.objects.get(pk=bang_id)
    members = bang.members.all()
    serializer = UserSerializer(members)
    return Response(serializer.data)
