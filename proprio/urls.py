#!/usr/bin/env python
from rest_framework import routers

from proprio.views import *

router = routers.DefaultRouter()
router.register('proprio', ProprioViewSet)
router.register('resi', ResiViewSet)
router.register('piece', PiecesResiViewSet)
router.register('image_de_la_piece', ImagePieceResiViewSet)
router.register('historique', HistoriqueViewSet)