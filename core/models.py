import uuid

from django.db import models
from datetime import datetime
import uuid


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=datetime.now(), null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=datetime.now(), null=True, blank=True)

    class Meta:
        abstract = True


class BaseUUIDModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True, editable=False)

    class Meta:
        abstract = True


class BaseModel(BaseUUIDModel, TimestampModel):
    class Meta:
        abstract = True
