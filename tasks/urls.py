from django.urls import include, path
from rest_framework import routers
from tasks import views

# api versioning
router = routers.DefaultRouter()
router.register(r"tasks", views.TaskView, "task")

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
