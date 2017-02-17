"""micro_bank_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from bank import views as bView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', bView.selfCheck, name='check'),
    url(r'^home/?$', bView.home, name='home'),
    url(r'login/?$', bView.signin, name='login'),
    url(r'logout/?$', bView.sign_out, name='logout'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]

# Adding the ability to save media files during uploads when we're still in debug mode. Once uploaded the below code won't be necessary as the server nginx and gunicorn will handle that.

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
