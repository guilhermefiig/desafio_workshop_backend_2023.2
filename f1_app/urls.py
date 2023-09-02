from rest_framework import routers
from .views import EquipeViewset, PilotosViewset

router = routers.DefaultRouter()

router.register(r'equipe', EquipeViewset)
router.register(r'pilotos', PilotosViewset)

urlpatterns = router.urls