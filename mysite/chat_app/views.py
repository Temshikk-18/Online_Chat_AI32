from rest_framework.generics import RetrieveUpdateAPIView

from .serializers import (UserProfileListSerializers, UserProfileDetailSerializers, HashTagSerializers, CitySerializers,
                          GroupSerializers, ChatGroupSerializers, PostSerializers, PostImageSerializers,
                          PostVideoSerializers, PersonalChatSerializers, StorySerializers, StoryMarkSerializers,
                          FollowingSerializers, FavoriteSerializers, HistorySerializers, CommentPostSerializers,
                          RegisterSerializer, LoginSerializer)
from rest_framework import viewsets, generics, status
from .models import (UserProfile, HashTag, City,
                     Group, ChatGroup, Post, PostImage, PostVideo, PersonalChat,
                     Story, StoryMark, Following, Favorite, History, CommentPost)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filter import UserFilter
from .pagination import PostPagination, CommentPostPagination

from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileListViewSet(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileListSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = UserFilter


class UserProfileDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializers


class HashTagViewSet(viewsets.ModelViewSet):
    queryset = HashTag.objects.all()
    serializer_class = HashTagSerializers


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializers


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers


class ChatGroupViewSet(viewsets.ModelViewSet):
    queryset = ChatGroup.objects.all()
    serializer_class = ChatGroupSerializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    pagination_class = PostPagination


class PostImageViewSet(viewsets.ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializers


class CommentPostViewSet(viewsets.ModelViewSet):
    queryset = CommentPost.objects.all()
    serializer_class = CommentPostSerializers
    pagination_class = CommentPostPagination


class PostVideoViewSet(viewsets.ModelViewSet):
    queryset = PostVideo.objects.all()
    serializer_class = PostVideoSerializers


class PersonalChatViewSet(viewsets.ModelViewSet):
    queryset = PersonalChat.objects.all()
    serializer_class = PersonalChatSerializers


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializers


class StoryMarkViewSet(viewsets.ModelViewSet):
    queryset = StoryMark.objects.all()
    serializer_class = StoryMarkSerializers


class FollowingViewSet(viewsets.ModelViewSet):
    queryset = Following.objects.all()
    serializer_class = FollowingSerializers


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializers


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializers

