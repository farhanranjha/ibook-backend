from django.urls import path, include

urlpatterns = [
    path('api/auth/', include('user.urls')),
    path('api/projects/', include('project.urls')),
]
