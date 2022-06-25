from django.contrib.auth.models import User
from django.db import models

from djangoresttest.api.models.base_models import BaseModel


class Item(BaseModel):
    name = models.CharField(blank=False, null=False, max_length=150)
    description = models.CharField(blank=True, max_length=400)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "items"
        ordering = ["-creation_datetime"]
