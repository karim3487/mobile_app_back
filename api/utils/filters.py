from django.apps import apps


def my_chats(qs, user):
    return qs.filter(participants__user=user).distinct()


def available_partners(qs, user):
    Participant = apps.get_model("api", "Participant")
    available_participants = Participant.objects.all().exclude(
        id__in=my_chats(qs, user).values(
            "participants")
    )
    return available_participants