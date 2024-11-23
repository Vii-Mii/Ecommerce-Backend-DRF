from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('products',views.ProductViewset)
router.register('collections',views.CollectionViewset)

urlpatterns = router.urls