from django.contrib import admin
from .models import Bull, Cow, Breeding, Message, User, Calf

# Register your models here.
admin.site.register(Bull)
admin.site.register(Cow)
admin.site.register(Breeding)
admin.site.register(Message)
admin.site.register(User)
admin.site.register(Calf)