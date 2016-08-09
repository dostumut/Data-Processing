"""data_processing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from web.views import calculations, visualization, run_amount_of_events_per_application, \
    poll_state, amount_of_events_result, run_amount_of_launch, amount_of_launch_result, run_amount_of_duplicates, \
    amount_of_duplicates_result

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', calculations, name='calculations'),
    url(r'^calculations/', calculations, name='calculations'),
    url(r'^visualization/', visualization, name='visualization'),
    url(r'^run_amount_of_events_per_application', run_amount_of_events_per_application),
    url(r'^run_amount_of_launch', run_amount_of_launch),
    url(r'^run_amount_of_duplicates', run_amount_of_duplicates),
    url(r'^poll_state', poll_state),
    url(r'^amount_of_events_result', amount_of_events_result),
    url(r'^amount_of_launch_result', amount_of_launch_result),
    url(r'^amount_of_duplicates_result', amount_of_duplicates_result),
]
