from rest_framework.response import Response
from rest_framework.decorators import api_view
#from base.models import Item
from base.models import Department
from .serializers import DepSerializer

@api_view(['GET'])
def getData(request):
    #items = Item.objects.all()
    departments = Department.objects.all()
    serializer = DepSerializer(departments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addDepartment(request):
    serializer = DepSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)