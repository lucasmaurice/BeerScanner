
from django.urls import include, path
from rest_framework import routers
from DrinkConsumption import api


router = routers.DefaultRouter()
router.register(r'containers', api.ContainerViewSet)
router.register(r'products', api.ProductViewSet)
router.register(r'products-container', api.ProductContainerViewSet)

urlpatterns = [
    path('api/scan/', api.tag_scan),
    path('api/', include(router.urls)),
]
