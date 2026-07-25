from .views import (UserProfileListViewSet, UserProfileDetailViewSet, HashTagViewSet,
                    CityViewSet, GroupViewSet,
                    ChatGroupViewSet, PostViewSet, PostImageViewSet, PostVideoViewSet,
                    PersonalChatViewSet, StoryViewSet, StoryMarkViewSet, FollowingViewSet,
                    FavoriteViewSet, HistoryViewSet, RegisterView, CustomLoginView, LogoutView,)
from rest_framework import routers
from django.urls import include, path

router = routers.DefaultRouter()


router.register('hash_teg', HashTagViewSet, basename='hash_teg')
router.register('city', CityViewSet, basename='city')
router.register('group', GroupViewSet, basename='group')
router.register('chat_group', ChatGroupViewSet, basename='chat_group')
router.register('post', PostViewSet, basename='post')
router.register('post_image', PostImageViewSet, basename='post_image')
router.register('post_video', PostVideoViewSet, basename='post_video')
router.register('personal_chat', PersonalChatViewSet, basename='personal_chat')
router.register('story', StoryViewSet, basename='story')
router.register('story_mark', StoryMarkViewSet, basename='story_mark')
router.register('following', FollowingViewSet, basename='following')
router.register('favorite', FavoriteViewSet, basename='favorite')
router.register('history', HistoryViewSet, basename='history')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),

    path('user_profile/', UserProfileListViewSet.as_view(), name='user_profile'),
    path('user_profile/<int:pk>/', UserProfileDetailViewSet.as_view(), name='user_profile_detail')
]