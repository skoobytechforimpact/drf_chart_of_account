"""Chart of Accounts URL Sets."""
from rest_framework.routers import DefaultRouter
from .views import LayerOneModelViewSet


router = DefaultRouter()
router.register(r'charts/layer/one', LayerOneModelViewSet, basename='layer_one_viewsets')
urlpatterns = router.urls
