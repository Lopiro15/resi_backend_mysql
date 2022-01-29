#!/usr/bin/env python
from rest_framework import routers

from client.views import ClientViewSet, CommandeViewSet, NoteViewSet, AjoutViewSet

router = routers.DefaultRouter()
router.register('client', ClientViewSet)
router.register('commande', CommandeViewSet)
router.register('notederesidence', NoteViewSet)
router.register('ajoutdesejour', AjoutViewSet)



