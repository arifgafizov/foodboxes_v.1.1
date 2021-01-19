from app_items.views import ItemViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('items', ItemViewset, basename='function-based')
urlpatterns = router.urls