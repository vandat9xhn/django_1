from django.urls import path
#
from .views import SubViewLC, SubLikeViewL, SubHistoryViewL

#


urlpatterns = [
    path('sub-lc', SubViewLC.as_view()),
    path('sub-like-l', SubLikeViewL.as_view()),
    path('sub-his-l', SubHistoryViewL.as_view()),
]
