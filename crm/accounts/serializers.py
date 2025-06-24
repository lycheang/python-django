from rest_framework import serializers
from .models import Account,Choice,Vote

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, read_only=True)

    class Meta:
        model = Choice
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)


    class Meta:
        model = Account
        fields = '__all__'