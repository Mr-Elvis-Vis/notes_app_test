from note.models import Note, NoteImage
from rest_framework import serializers


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Note


class NoteImageSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    image_url = serializers.URLField(
        allow_blank=False,
    )

    class Meta:
        fields = '__all__'
        model = NoteImage
