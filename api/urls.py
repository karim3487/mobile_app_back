from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views as api_app

router = DefaultRouter()
router.register("auth",
                api_app.auth.AuthViewSet,
                basename="auth")
router.register("users",
                api_app.user.UserViewSet,
                basename="user")
router.register("ads",
                api_app.ad.AdViewSet,
                basename="ad")
router.register("chats",
                api_app.chat.ChatViewSet,
                basename="chat")
router.register("attachments",
                api_app.attachment.AttachmentViewSet,
                basename="attachment")
router.register("teachers",
                api_app.teacher.TeacherViewSet,
                basename="teacher")
# router.register("timetable",
#                 api_app.timetable.TimetableWeekView,
#                 basename="timetable")

timetables = [
    path("<str:code>", api_app.timetable.TimetableWeekView.as_view(),
         name="timetable-by-week")
              ]

urlpatterns = [
    path("timetables/", include(timetables))
]

urlpatterns += router.urls
