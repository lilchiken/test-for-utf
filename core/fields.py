from django.db import models


class CustomCharField(models.CharField):

    def __init__(self, *args, **kwargs) -> None:
        kwargs['max_length'] = 255
        kwargs['blank'] = True
        kwargs['null'] = True
        super().__init__(*args, **kwargs)


class NamedCharField(models.CharField):

    def __init__(self, *args, **kwargs) -> None:
        kwargs.setdefault('verbose_name', 'Название на русском')
        kwargs['max_length'] = 255
        super().__init__(*args, **kwargs)
