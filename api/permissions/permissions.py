from abc import ABCMeta, abstractmethod

from django.db.models import Q
from rest_access_policy import AccessPolicy

from api.utils import filters as api_filters

class BaseAccessPolicy(AccessPolicy):
    __metaclass__ = ABCMeta

    # statements = []

    @classmethod
    @abstractmethod
    def scope_queryset(cls, request, queryset, action):
        pass


class ChatAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["mychats"],
            "principal": "authenticated",
            "effect": "allow"
        },
        {
            "action": ["send_message"],
            "principal": "authenticated",
            "effect": "allow",
            "condition": "is_participant"
        },
        {
            "action": ["available_partners"],
            "principal": "authenticated",
            "effect": "allow"
        }
    ]

    @classmethod
    def scope_queryset(cls, request, qs, action):
        if action in ["mychats", "send_message"]:
            return api_filters.my_chats(qs, request.user)

    def is_participant(self, request, view, action) -> bool:
        return bool(view.get_object().participants.filter(user=request.user))


class UserAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve", "available_partners", "my_partners"],
            "principal": "authenticated",
            "effect": "allow"
        },
        {
            "action": ["start_conversation"],
            "principal": "authenticated",
            "effect": "allow"
        }
    ]

    @classmethod
    def scope_queryset(cls, request, qs, action):
        return qs


class AttachmentAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": "authenticated",
            "effect": "allow"
        }
    ]

    @classmethod
    def scope_queryset(cls, request, qs, action):
        return qs
