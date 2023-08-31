from rest_framework import serializers
from .models import RoomCategory, Room


class RoomCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoomCategory
        fields = "__all__"


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.HyperlinkedRelatedField(
        view_name="roomcategory-detail",
        read_only=True
    )
    class Meta:
        model = Room
        fields = '__all__'