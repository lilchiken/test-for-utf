from rest_framework import (
    viewsets,
    mixins
)


class ListModelViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Ограничиваем методы к viewset'у."""

    pass
