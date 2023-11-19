from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index),
    path("settings/", admin.site.urls),
    path('sign-in/', auth_views.LoginView.as_view(
        template_name="core/login.html",
        )
    ),
    path('sign-out/', auth_views.LogoutView.as_view(next_page="/")),
    path("api/", include("restapi.urls")),
    path("swagger/", include("swagger.urls")),
    path("service-desk/", include("servicedesk.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
