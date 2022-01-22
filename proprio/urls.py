#!/usr/bin/env python
from rest_framework import routers

from proprio.views import HistoriqueViewSet, ImageResiViewSet, ProprioViewSet, ResiViewSet

router = routers.DefaultRouter()
router.register('proprio', ProprioViewSet)
router.register('resi', ResiViewSet)
router.register('image', ImageResiViewSet)
router.register('historique', HistoriqueViewSet)