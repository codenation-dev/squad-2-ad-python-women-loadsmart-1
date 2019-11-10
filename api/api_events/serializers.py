from rest_framework import serializers

from api.models import Event


class EventSerializer(serializers.ModelSerializer):

    address = serializers.SerializerMethodField('get_address_from_agent')
    env = serializers.SerializerMethodField('get_environment_from_agent')
    version = serializers.SerializerMethodField('get_version_from_agent')

    class Meta:
        model = Event
        fields = ['title', 'details', 'level', 'address', 'env', 'version']

    def get_address_from_agent(self, event):
        address = event.agent.address
        return address

    def get_environment_from_agent(self, event):
        environment = event.agent.env.name
        return environment

    def get_version_from_agent(self, event):
        version = event.agent.version
        return version
