from django.urls import path, include, re_path
from django.views.generic import TemplateView
from .views import *


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
    path('update-profile/', update_user_profile, name='update')
]

# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
