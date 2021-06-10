from django.urls import path
#
from . import views
#
from .child_app.basis import urls as basis_url
from .child_app.contact import urls as contact_url
from .child_app.life_event import urls as life_event_url
from .child_app.picture import urls as picture_url
from .child_app.placed import urls as placed_url
from .child_app.relation import urls as relation_url
from .child_app.work import urls as work_url
from .child_app.you import urls as you_url

#


urlpatterns = [
    # path('profile-l/', views.ProfileViewL.as_view()),
    path('profile-r/<int:pk>/', views.ProfileViewR.as_view()),
    path('name-u/', views.NameViewU.as_view()),
    path('personal-setting-u/', views.PersonalSettingViewU.as_view()),

    *basis_url.urlpatterns,
    *contact_url.urlpatterns,
    *life_event_url.urlpatterns,
    *picture_url.urlpatterns,
    *placed_url.urlpatterns,
    *relation_url.urlpatterns,
    *work_url.urlpatterns,
    *you_url.urlpatterns,
]
