from django.contrib import admin
from .models import Bull, Cow, Breeding, Message, Calf

# Register your models here.
admin.site.register(Bull)
admin.site.register(Cow)
admin.site.register(Breeding)
admin.site.register(Calf)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_id', 'user_profile', 'sent_on', 'short_message', 'read')
    list_filter = ('read', 'sent_on')
    search_fields = ('user_profile__username', 'message')
    actions = ['mark_as_read', 'mark_as_unread']

    def short_message(self, obj):
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
    short_message.short_description = 'Message'

    def mark_as_read(self, request, queryset):
        queryset.update(read=True)
    mark_as_read.short_description = "Mark selected messages as read"

    def mark_as_unread(self, request, queryset):
        queryset.update(read=False)
    mark_as_unread.short_description = "Mark selected messages as unread"

admin.site.register(Message, MessageAdmin)