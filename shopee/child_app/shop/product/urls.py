from django.urls import path
#
from . import views
#
from .comment.urls import urlpatterns as comment_urls
from .rate.urls import urlpatterns as rate_urls

#

urlpatterns = [
    *comment_urls,
    *rate_urls,
    path('product-l/', views.ProductViewL.as_view()),
]
