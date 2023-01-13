from rest_framework import serializers
#from base.models import BaseItem
from base.models import Department

class DepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'