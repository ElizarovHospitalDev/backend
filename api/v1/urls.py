from django.urls import include, path


urlpatterns = [
    path('users/', include('api.v1.users.urls')),
    path('treatments/', include('api.v1.treatments.urls')),
    path('endoprosthetics/', include('api.v1.endoprosthetics.urls')),
]
