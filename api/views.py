from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import *
from api.models import Note


@api_view(["GET"])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getNote(request, pk):
    note = Note.objects.get(pk=pk)
    serializer = NoteSerializer(note)
    return Response(serializer.data)


@api_view(["POST"])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(note, many=False)

    return Response(serializer.data)


@api_view(["PUT"])
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(pk=pk)
    serializer = NoteSerializer(note, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(["GET"])
def deleteNote(request, pk):
    note = Note.objects.get(pk=pk)
    note.delete()

    return Response("Note was deleted")


@api_view(["GET"])
def getRoutes(request):
    routes = [
        {
            'name': 'Anket',

        },
        {
            'name': "Richa",
        },
    ]
    return Response(routes)
