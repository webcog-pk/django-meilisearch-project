from rest_framework import serializers
from core.models import Person

class PersonSearializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"