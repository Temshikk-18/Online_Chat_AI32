from django.contrib import admin

from .models import (UserProfile, HashTag, City,
                     Group, ChatGroup, Post, PostImage, PostVideo, PersonalChat,
                     Story, StoryMark, Following, Favorite, History)

class StoryMarkInline(admin.TabularInline):
    model = StoryMark
    extra = 1

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1

class PostVideoInline(admin.TabularInline):
    model = PostVideo
    extra = 1

class ChatGroupInline(admin.TabularInline):
    model = ChatGroup
    extra = 1

class StoryAdmin(admin.ModelAdmin):
    inlines = [StoryMarkInline]

class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline, PostVideoInline]

class GroupInline(admin.ModelAdmin):
    inlines = [ChatGroupInline]


admin.site.register(UserProfile)
admin.site.register(HashTag)
admin.site.register(City)
admin.site.register(Group)
admin.site.register(Post, PostAdmin)
admin.site.register(PersonalChat)
admin.site.register(Story, StoryAdmin)
admin.site.register(Following)
admin.site.register(Favorite)
admin.site.register(History)



