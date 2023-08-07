from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import Projectserializer
from projects.models import project



@api_view(['GET'])
def getRoutes(request):

    routes = [
        {"GET":'/api/projects'},
        {"GET":'/api/projects/id'},
        {"POST":'/api/projects/id/vote'},

        {"POST":'/api/users/token'},
        {"POST":'/api/users/token/refresh'},
    ]

    return Response( routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getprojects(request):

    print('USER:', request.user )

    projects = project.objects.all()
    serializer = Projectserializer(projects, many=True)

    return Response(serializer.data)



@api_view(['GET'])
def getproject(request, pk):

    Project = project.objects.get(id=pk)
    serializer = Projectserializer(Project, many=False)

    return Response(serializer.data)