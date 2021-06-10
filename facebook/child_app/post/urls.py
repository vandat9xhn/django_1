from django.urls import path
#
from .views import PostViewL
#
from .comment.urls import urlpatterns as cmt_urls
from .vid_pic.urls import urlpatterns as vp_urls
from .like_share.urls import urlpatterns as like_share_urls
from .history.urls import urlpatterns as his_urls

#


urlpatterns = [
    path('post-l/', PostViewL.as_view()),
    *cmt_urls,
    *vp_urls,
    *like_share_urls,
    *his_urls
]
