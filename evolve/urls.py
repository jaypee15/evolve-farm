from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('mlm.urls')),
    path("api-auth/", include("rest_framework.urls")),
    path("api/dj-rest-auth/", include("dj_rest_auth.urls")),
    path("api/v1/dj-rest-auth/registration/", 
        include("dj_rest_auth.registration.urls")),
]
