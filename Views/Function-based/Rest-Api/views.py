# django restframework
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ApiApp.models import Advocates
from .serializers import AdvocateSerializer

from django.db.models import Q
# Create your views here.

@api_view(['GET'])
def api(request):
    data = ['welcome/', 'advocates' ,'advocates/username']
    return Response(data)

@api_view(['GET', 'POST'])
def advocate_list(request):

    if request.method == 'GET':
        query = request.GET.get('query')
        if query == None:
            query = ''
            
        print('Query', query)

        advocates = Advocates.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)

    else:
        if request.method == 'POST':
            advocate = Advocates.objects.create(
                username=request.data['username'],
                name=request.data['name']
            )

            serializer = AdvocateSerializer(advocate, many=False)

            print(request.data)
            print('data saved to database')
            # return Response('Post request')
            return Response(serializer.data)
        
@api_view(['GET', 'PUT', 'DELETE'])
def advocate_detail(request, username):
    advocate = Advocates.objects.get(username=username)

    if request.method == 'GET':
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        advocate.username = request.data['username']
        advocate.name = request.data['name']
        advocate.save()
        print('data updated')

        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    if request.method == 'DELETE':
        advocate.delete()
        print('data deleted')
        return Response('User '+ str(advocate.username) +' was deleted')
