#!/usr/bin/env python
from rest_framework import routers

from client.views import ClienViewSet, CommandeViewSet, NoteViewSet, AjoutViewSet

router = routers.DefaultRouter()
router.register('client', ClienViewSet)
router.register('commande', CommandeViewSet)
router.register('notederesidence', NoteViewSet)
router.register('ajoutdesejour', AjoutViewSet)



