from django.db import models


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deletion_datetime__isnull=True)


class BaseModel(models.Model):
    creation_datetime = models.DateTimeField(auto_now_add=True)
    deletion_datetime = models.DateTimeField(null=True)

    _objects = models.Manager()  # Default Django manager
    objects = BaseManager()  # Non deleted objects manager

    class Meta:
        abstract = True
