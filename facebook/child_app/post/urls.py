from django.urls import path
from django.db.models import QuerySet
#
from . import views
#
from .comment.urls import urlpatterns as cmt_urls
from .vid_pic.urls import urlpatterns as vp_urls
from .like_share.urls import urlpatterns as like_share_urls
from .history.urls import urlpatterns as his_urls

#


urlpatterns = [
    path('post-lc/', views.PostViewLC.as_view()),
    path('post-rud/<int:pk>/', views.PostViewRUD.as_view()),
    path('post-permission-u/<int:pk>/', views.PostPerMissionViewU.as_view()),

    *cmt_urls,
    *vp_urls,
    *like_share_urls,
    *his_urls
]
