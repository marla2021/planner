from django.contrib import admin
from django.urls import path, include, re_path

from todolist.urls import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('', include('social_django.urls', namespace='social')),
    path('core/', include('core.urls')),
    path('goals/', include('goals.urls')),
    re_path(r'^swagger/$',schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]