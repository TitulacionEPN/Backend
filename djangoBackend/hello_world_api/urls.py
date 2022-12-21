from .viewsets import StudentViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('students', StudentViewSet)

urlpatterns = router.urls
