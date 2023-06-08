from rest_framework import (
    viewsets,
    mixins
)


class ListModelViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    pass
