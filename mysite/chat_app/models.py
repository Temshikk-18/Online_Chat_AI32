from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(region='KG', default='+996')
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)


class HashTag(models.Model):
    hashtag_name = models.CharField(max_length=32)

    def __str__(self):
        return self.hashtag_name


class City(models.Model):
    city_name = models.CharField(max_length=32)
    city_url = models.URLField()

    def __str__(self):
        return self.city_name


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_posts')
    text = models.TextField(null=True, blank=True)
    hashtag = models.ManyToManyField(HashTag, null=True, blank=True, related_name='hashtag')
    city = models.ManyToManyField(City, null=True, blank=True, related_name='city')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.text}'


class PostVideo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    video = models.FileField(upload_to='video_post/', null=True, blank=True)


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image_post/', null=True, blank=True)


class CommentPost(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()


class Story(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='owner_story')
    image = models.ImageField(upload_to='images_story/', null=True, blank=True)
    video = models.FileField(upload_to='videos_story/', null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.image} | {self.video} | {self.text}'


class StoryMark(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, null=True, blank=True, related_name='stories')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name='owner')

    def __str__(self):
        return f'{self.user}: {self.story}'


class History(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_history')
    story = models.ForeignKey(StoryMark, on_delete=models.CASCADE, related_name='story_history')

    def __str__(self):
        return f'{self.user}: {self.story}'


class Following(models.Model):
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='following')

    def __str__(self):
        return f'{self.follower}: {self.following}'


class Favorite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_favorite')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')
    like = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}: {self.post}'


class Group(models.Model):
    group_name = models.CharField(max_length=32)
    group_image = models.ImageField(upload_to='group_images/', null=True, blank=True)
    members = models.ManyToManyField(UserProfile, related_name='members')

    def __str__(self):
        return self.group_name


class ChatGroup(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group')
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='personal_images/', null=True, blank=True)
    video = models.FileField(upload_to='personal_videos/', null=True, blank=True)
    voice = models.FileField(upload_to='personal_chat_voices', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'


class PersonalChat(models.Model):
    user_1 = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_1')
    user_2 = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_2')
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='personal_images/', null=True, blank=True)
    video = models.FileField(upload_to='personal_videos/', null=True, blank=True)
    voice = models.FileField(upload_to='personal_chat_voices', null=True, blank=True)

    def __str__(self):
        return f'{self.user_1}/ {self.user_2}'







