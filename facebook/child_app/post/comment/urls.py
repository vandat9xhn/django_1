from django.urls import path
#
from . import views
#
from .sub.urls import urlpatterns as sub_urls

#


urlpatterns = [
    path('cmt-lc/', views.CommentViewLC.as_view()),
    path('cmt-ud/<int:pk>/', views.CommentViewUD.as_view()),

    path('cmt-like-lc/', views.CmtLikeViewLC.as_view()),

    path('cmt-his-l/', views.CmtHistoryViewL.as_view()),

    *sub_urls,
]
