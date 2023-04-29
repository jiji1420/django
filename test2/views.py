from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from . import serializers


# Create your views here.

@api_view(['GET'])
def person_list(request):
    vse_ludi = Person.objects.all()
    serializer = serializers.PersonSerializers(vse_ludi, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def person_detail(request,pk):
    try:
        queryset = Person.objects.get(id=pk)
        serializer = serializers.PersonSerializers(queryset)
        print(serializer.data)
        return Response(serializer.data, status=200)
    except Person.DoesNotExist:
        return Response(f'таска от id {pk} нет', status=404)


@api_view(['POST'])
def person_create(request):
    print(request.data, '========')
    serializer = serializers.PersonSerializers(data=request.data)
    # print(serializer)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)

@api_view(['DELETE'])
def person_delete(request,pk):
    try:
        person = Person.objects.get(id=pk)
        person.delete()
        return Response('Deleted Successfully', status=204)
    except Person.DoesNotExist:
        return Response(f'This person with {pk} it does not exist', status=404)


@api_view(['PUT', 'PATCH'])
def person_update(request, pk):
    try:
        person = Person.objects.get(id=pk)
        if request.method == 'PUT':
            serializer = serializers.PersonSerializers(instance=person, data=request.data)
        else:
            serializer = serializers.PersonSerializers(instance=person, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=206)
    except Person.DoesNotExist:
        return Response('Does not exist', status=404)
