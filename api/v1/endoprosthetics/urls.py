from rest_framework.routers import SimpleRouter

from api.v1.endoprosthetics import views


router = SimpleRouter()

router.register('vendors', views.EndoprostheticVendorViewSet)
router.register('types', views.EndoprostheticTypeViewSet)
router.register('forms', views.EndoprostheticFormViewSet)
router.register('', views.EndoprostheticViewSet)

urlpatterns = router.urls
