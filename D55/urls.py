from django.contrib import admin
from django.urls import path, reverse_lazy, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('p_library.urls', namespace='p_library')),
    path('accounts/', include('allauth.urls')),
]



