from model_utils.models import TimeStampedModel


class NamedTimeStampedModel(TimeStampedModel):

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name_ru
