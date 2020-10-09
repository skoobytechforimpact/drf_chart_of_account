"""Chart of Accounts Layers Models and Classes."""
from django.db import models
from django.contrib.auth import get_user_model
import uuid


# Create your models here.
class LayersBaseModel(models.Model):
    """This is the abstract base class for all the layer models.

    All other layer model classes will extend this class. Only difference is
    the child layer class will override a foreign key relation key with it's
    parent class
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='ID')
    serial_no = models.AutoField(primary_key=False, unique=True, verbose_name='Serial No.')
    name = models.CharField(max_length=80, null=False, blank=False, verbose_name='Layer Name')
    ref_no = models.IntegerField(null=False, blank=False, default=1, verbose_name='Reference No.')
    is_active = models.BooleanField(default=True, verbose_name='Active')
    created_by = models.ForeignKey(get_user_model(), related_name='layer_created_by', verbose_name='Created by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        """Meta data class for the base model."""

        verbose_name = 'LayersBaseModel'
        verbose_name_plural = 'LayersBaseModels'
        abstract = True
        ordering = ['name']
