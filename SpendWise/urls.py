
from django.contrib import admin
from django.urls import path,include
from tracker.views import register_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tracker.urls')),
    path('accounts/register/', register_view, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout
]
