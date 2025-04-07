from rest_framework import serializers
from .models import Watchlist,StremPlatform

class WatchListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length=50)
    storyline=serializers.CharField(max_length=50)
    # platform = serializers.ForeignKey(StremPlatform,on_delete=serializers.CASCADE)
    active = serializers.BooleanField(default =True)
    created = serializers.DateTimeField()

    def create(self, validated_data):

        return Watchlist.objects.create(validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `watchlist` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.storyline = validated_data.get('storyline', instance.storyline)
        instance.active = validated_data.get('linenos', instance.linenos)
        instance.created = validated_data.get('language', instance.language)
        instance.save()
        return instance


class stremPlatformserializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length=50)
    about = serializers.CharField(max_length=100)
    website = serializers.CharField(max_length=100)

    def create(self, validated_data):

        return Watchlist.objects.create(validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `stemplatform` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.about = validated_data.get('about', instance.about)
        instance.webbsite = validated_data.get('webbsite', instance.webbsite)
        instance.save()
        return instance
