from django.urls import path
#
from .views import VidPicCmtViewLC, VidPicCmtLikeViewL, VidPicCmtHistoryViewL
#
from .sub.urls import urlpatterns as sub_urls

#


urlpatterns = [
    path('vid-pic-cmt-lc', VidPicCmtViewLC.as_view()),
    path('vid-pic-cmt-like-l', VidPicCmtLikeViewL.as_view()),
    path('vid-pic-cmt-his-l', VidPicCmtHistoryViewL.as_view()),
    *sub_urls,
]
