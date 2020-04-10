from django.urls import include, path
from rest_framework import routers
from myproject.core import views as v


app_name = 'core'


router = routers.DefaultRouter()
router.register('language', v.LanguageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
