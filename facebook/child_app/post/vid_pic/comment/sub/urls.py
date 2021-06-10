from django.urls import path
#
from .views import VidPicSubViewLC, VidPicSubLikeViewL, VidPicSubHistoryViewL

#


urlpatterns = [
    path('vid-pic-sub-lc', VidPicSubViewLC.as_view()),
    path('vid-pic-sub-like-l', VidPicSubLikeViewL.as_view()),
    path('vid-pic-sub-his-l', VidPicSubHistoryViewL.as_view()),
]
