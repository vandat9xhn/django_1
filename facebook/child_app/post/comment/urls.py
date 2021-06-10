from django.urls import path
#
from .views import CommentViewLC, CmtLikeViewL, CmtHistoryViewL
#
from .sub.urls import urlpatterns as sub_urls

#


urlpatterns = [
    path('cmt-lc', CommentViewLC.as_view()),
    path('cmt-like-l', CmtLikeViewL.as_view()),
    path('cmt-his-l', CmtHistoryViewL.as_view()),
    *sub_urls,
]
