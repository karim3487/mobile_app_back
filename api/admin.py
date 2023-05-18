from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Attachment
from .models.chat import Chat, Participant
from .models.teachers import Teacher
from .models.user import User
from .models.ad import Ad
from .models.message import Message


class MyUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "id")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
    readonly_fields = ["date_joined"]
    fieldset = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": (
            "email",
            "first_name",
            "last_name",
            "surname",
            "profession",
        )
        }),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name", "last_name", "surname", "profession", "password1", "password2"),
            },
        ),
    )


class AdAdmin(admin.ModelAdmin):
    list_display = ("creator", "title", "created_at", "id")
    autocomplete_fields = (
        "creator",
    )
    search_fields = ("creator", "title")


class ChatAdmin(admin.ModelAdmin):
    search_fields = ("id", )


class ParticipantAdmin(admin.ModelAdmin):
    autocomplete_fields = (
        "chat",
        "user",
    )
    list_display = ("chat", "user", "created_at", "id")
    search_fields = ("user", )
    list_filter = ("chat", )


class MessageAdmin(admin.ModelAdmin):
    autocomplete_fields = (
        "sender",
        "chat",
    )
    list_display = ("sender", "chat", "created_at", "id")
    search_fields = ("sender", "chat")
    list_filter = ("sender", "chat")


admin.site.register(User, MyUserAdmin)
admin.site.register(Ad, AdAdmin)
admin.site.register(Chat, ChatAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Attachment)
admin.site.register(Teacher)

