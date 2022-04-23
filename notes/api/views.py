import base64
import datetime

from api.permissions import IsAuthor
from api.serializers import NoteImageSerializer, NoteSerializer
from django.shortcuts import get_object_or_404
from note.models import Note, NoteImage, TemporaryImage
from rest_framework import viewsets


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthor]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        author = self.request.user
        return Note.objects.filter(author=author)


class NoteImageViewSet(viewsets.ModelViewSet):
    serializer_class = NoteImageSerializer
    permission_classes = [IsAuthor]

    def perform_create(self, serializer):
        note = get_object_or_404(Note, pk=self.kwargs.get('note_id'))
        serializer.save(author=self.request.user, note=note)

    def get_queryset(self):
        note = get_object_or_404(Note, pk=self.kwargs.get('note_id'))
        return NoteImage.objects.filter(note=note)
