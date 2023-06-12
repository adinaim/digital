from urllib import request
from rest_framework import serializers
from django.db.models import Avg
# from apps.review.serializers import CommentSerializer, LikeSerializer
from django.contrib.auth import get_user_model

from .models import Location, LocationImage #, ConcreteTour
from apps.business.models import BusinessProfile
from django.contrib.auth import get_user_model


User = get_user_model()

class LocationCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    # company_name = serializers.ReadOnlyField()

    class Meta:
        model = Location
        fields = '__all__'
        # exclude = ['tour_image_carousel']

    tour_image_carousel = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )
    # tour = Tour.objects.first()
    # print(tour.company_name)

    def create(self, validated_data):
        avatar_carousel = validated_data.pop('tour_image_carousel')
        tour = Location.objects.create(**validated_data)
        images = []
        for image in avatar_carousel:
            images.append(LocationImage(tour=tour, image=image))
        LocationImage.objects.bulk_create(images)
        tour.save()

        user = self.context['request'].user
        # attrs['user'] = user
        # print(user)
        # print(type(user))

        # print(user.profile)
        # company_name = user.profile.title

        # print(type(user.profile))
        # print(attrs['user'])
        # validated_data['company_name'] = user.profile
        # company_name = user.profile
        # print('val', validated_data['company_name'])
        # print(tour.company_name)

        return tour#, company_name

    def validate(self, attrs):#, validated_data):
        user = self.context['request'].user
        attrs['user'] = user
        # print(attrs['user'])
        # company_name = user.profile
        # validated_data['company_name'] = user.profile
        # company_name = user.profile.title
        # attrs['company_name'] = company_name
        # print('attrs', attrs['company_name'])
        # print('attrs', type(attrs['company_name']))
        # print(attrs)
        return attrs#, validated_data


# circuits = Circuits.objects.filter(site_data__id=1)
# for cm in circuits:
#     maintenances = cm.maintenance.all()
#     for maintenance in maintenances:
#          print(maintenance )

    # def create(self, validated_data):
    #     tour = Tour.objects.create(**validated_data)
    #     tour.user = None
    #     request = self.context.get("request")
    #     if request and hasattr(request, "user"):
    #         tour.user = request.user
    #     self.save()

    def validate(self, attrs):
        user = self.context['request'].user
        attrs['user'] = user
        return attrs

        





    

        
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['comments'] = CommentSerializer(
    #         instance.comments.all(), many=True
    #     ).data

    
class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['carousel'] = LocationImageSerializer(
            instance.tour_images.all(), many=True
        ).data
        return representation


class LoationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['title', 'image', 'place', 'level', 'number_of_days', 'company_name']

                                                                                                        # commented
# class ConcreteTourCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ConcreteTour
#         fields = '__all__'

#     def create(self, validated_data):
#         # return super().create(validated_data)
#         tour = ConcreteTour.objects.create(**validated_data)
#         return tour

    


# class ConcreteTourSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ConcreteTour
#         fields = '__all__'

#     def to_representation(self, instance):
#         rep = super().to_representation(instance)
#         # rep['rating'] = RatingSerializer(
#         #     instance.rating_tour.all(),
#         #     many=True
#         # ).data
#         rating = instance.rating_tour.aggregate(Avg('rating'))['rating__avg']
#         rep['comments'] = CommentSerializer(
#             instance.comment_tour.all(),
#             many=True
#         ).data
#         rep['likes'] = instance.like_tour.all().count()
#         rep['liked_by'] = LikeSerializer(instance.like_tour.all().only('user'), many=True).data
#         if rating:
#             rep['rating'] = round(rating,1)
#         else:
#             rep['rating'] = 0.0
#         return rep

# class ConcreteTourListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ConcreteTour
#         fields = '__all__'

    
# class TourImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TourImage
#         fields = 'image',