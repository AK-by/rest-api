from rest_framework import serializers
from . models import SimpleMessages


class SimpleMessagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SimpleMessages
        fields = ('pk', 'title', 'message', 'created')
