# serializers.py
from rest_framework import serializers
from .models import JarCount, ShiftTiming

class JarCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = JarCount
        fields = ['id', 'count', 'timestamp', 'shift1_start', 'shift2_start']

class ShiftTimingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftTiming
        fields = ['shift1_start', 'shift2_start']
