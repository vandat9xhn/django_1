"""react_django_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import settings
from django.conf.urls.static import static


#

class CustomTemplateView(TemplateView):

    def get_context_data(self, **kwargs):
        return 'this is context'

#


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/account/', include('account.urls')),
    path('api/profile/', include('user_profile.urls')),
    path('api/friend/', include('friend.urls')),
    path('api/notice/', include('notice.urls')),

    path('api/facebook/', include('facebook.urls')),
    path('api/shopee/', include('shopee.urls')),
    path('api/phone/', include('phone_lap.urls')),
    path('api/chat/', include('chat.urls')),
    path('api/city/', include('city.urls')),
]

#

page_urls = ['', 'home', 'phone-laptop']

for page_url in page_urls:
    urlpatterns += [
        path(page_url, TemplateView.as_view(template_name='index.html'))
    ]

#

if settings.DEBUG or True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
