"""Chart of Accounts Layers Models and Classes."""
from django.db import models
import uuid


# Create your models here.
class LayersBaseModel(models.Model):
    """This is the abstract base class for all the layer models.

    All other layer model classes will extend this class. Only difference is
    the child layer class will override a foreign key relation key with it's
    parent class
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=80, null=False, blank=False, verbose_name='Layer Name')
