from .models import (UserProfile, HashTag, City,
                     Group, ChatGroup, Post, PostImage, PostVideo, PersonalChat,
                     Story, StoryMark, Following, Favorite, History, CommentPost)
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age',
                  'phone_number']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }



class UserProfileListSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username']


class UserProfileDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class HashTagSerializers(serializers.ModelSerializer):
    class Meta:
        model = HashTag
        fields = '__all__'


class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class GroupSerializers(serializers.ModelSerializer):
    members = UserProfileListSerializers(read_only=True, many=True)
    class Meta:
        model = Group
        fields = ['id', 'group_name', 'group_image', 'members']


class ChatGroupSerializers(serializers.ModelSerializer):
    user = UserProfileListSerializers(read_only=True)
    group = GroupSerializers(read_only=True)
    class Meta:
        model = ChatGroup
        fields = ['id', 'text', 'image', 'video', 'voice', 'created_at', 'user', 'group']


class PostSerializers(serializers.ModelSerializer):
    user_posts = UserProfileListSerializers(read_only=True, source='user')
    hashtag = HashTagSerializers(read_only=True, many=True)
    city = CitySerializers(read_only=True, many=True)
    class Meta:
        model = Post
        fields = ['id', 'text', 'created_at', 'user_posts', 'hashtag', 'city']


class PostImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'


class CommentPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommentPost
        fields = '__all__'


class PostVideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostVideo
        fields = '__all__'


class PersonalChatSerializers(serializers.ModelSerializer):
    user_1 = UserProfileListSerializers(read_only=True)
    user_2 = UserProfileListSerializers(read_only=True)
    class Meta:
        model = PersonalChat
        fields = ['id', 'text', 'image', 'video', 'voice', 'user_1', 'user_2']


class StorySerializers(serializers.ModelSerializer):
    owner_story = UserProfileListSerializers(read_only=True, source='user')
    class Meta:
        model = Story
        fields = ['id', 'image', 'video', 'text', 'created_at', 'owner_story']


class StoryMarkSerializers(serializers.ModelSerializer):
    stories = StorySerializers(read_only=True, source='story')
    owner = UserProfileListSerializers(read_only=True, source='user')
    class Meta:
        model = StoryMark
        fields = ['id', 'stories', 'owner']


class FollowingSerializers(serializers.ModelSerializer):
    follower = UserProfileListSerializers(read_only=True)
    following = UserProfileListSerializers(read_only=True)
    class Meta:
        model = Following
        fields = ['id', 'follower', 'following']


class FavoriteSerializers(serializers.ModelSerializer):
    user_favorite = UserProfileListSerializers(read_only=True, source='user')
    posts = PostSerializers(read_only=True, source='post')
    class Meta:
        model = Favorite
        fields = ['id', 'like', 'user_favorite', 'posts']


class HistorySerializers(serializers.ModelSerializer):
    user_history = UserProfileListSerializers(read_only=True, source='user')
    story_history = StorySerializers(read_only=True, source='story')
    class Meta:
        model = History
        fields = ['id', 'user_history', 'story_history']



