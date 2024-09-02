
from rest_framework import serializers
from .models import Task, Campaign, Member

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    campaign = CampaignSerializer()
    trainer = MemberSerializer()
    lead = MemberSerializer()

    class Meta:
        model = Task
        fields = '__all__'