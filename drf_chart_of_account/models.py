"""Chart of Accounts Layers Models and Classes."""
from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from .apps import DrfChartOfAccountConfig
import uuid


# Create your models here.
class LayersBaseModel(models.Model):
    """This is the abstract base class for all the layer models.

    All other layer model classes will extend this class. Only difference is
    the child layer class will override a foreign key relation key with it's
    parent class
    """

    name = models.CharField(max_length=80, null=False, blank=False, verbose_name='Layer Name')
    ref_no = models.CharField(max_length=80, null=False, blank=False, unique=True, verbose_name='Reference No.')
    is_active = models.BooleanField(default=True, verbose_name='Active')
    created_by = models.ForeignKey(get_user_model(), related_name='layer_created_by', verbose_name='Created by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        """Meta data class for the base model."""

        db_table = str(DrfChartOfAccountConfig.name) + '_layers_base_table'
        verbose_name = 'Layers Base Model'
        verbose_name_plural = 'Layers Base Models'
        abstract = True
        ordering = ['name']

    def __str__(self):
        """Return the string representation of the model."""
        return self.name

    def get_ref_no(self, layer_no):
        """Calculate the reference number of the instance."""
        if layer_no > 1:
            index_num = layer_no - 1
            parent_ref_no = self.parent_layer.ref_no.split('.')
            parent_ref_no[index_num] = str(self.pk)
            return ".".join(parent_ref_no)
        else:
            return str(self.pk) + '.0.0.0.0'

    def validate_transaction(self, related_object_name=None):
        """Check if transaction exists of the instance."""
        if related_object_name is not None:
            if getattr(self, related_object_name).exists():
                raise PermissionDenied('The selected layer has transactions')
        return True

    def validate_child_relation(self, related_object_name):
        """Check if related object exists of the instance."""
        try:
            if getattr(self, related_object_name).exists():
                raise PermissionDenied('The selected layer has child object')
        except AttributeError:
            return True
        return True

    def delete(self, related_object_name):
        """Check child and transaction relations."""
        if self.validate_child_relation(related_object_name):
            if self.validate_transaction():
                return super(LayersBaseModel, self).delete()

    def validate_update(self, related_object_name):
        """Check and validate child and transaction relations.

        A custom method needed to be called each update operations.
        """
        if self.validate_child_relation(related_object_name):
            if self.validate_transaction():
                return True


class LayerOneModel(LayersBaseModel):
    """This is the parent class for all the layers."""

    created_by = models.ForeignKey(get_user_model(), related_name='layer_one_created_by', verbose_name='Created by', on_delete=models.CASCADE)

    class Meta(LayersBaseModel.Meta):
        """Meta data extending from parent Meta class."""

        db_table = str(DrfChartOfAccountConfig.name) + '_layer_one_table'
        verbose_name = 'Layer One Model'
        verbose_name_plural = 'Layer One Models'
        abstract = False

    def save(self, *args, **kwargs):
        """Set the ref_no and save the data to the model."""
        self.ref_no = str(uuid.uuid4())
        super(LayerOneModel, self).save(*args, **kwargs)
        self.ref_no = self.get_ref_no(1)
        return super(LayerOneModel, self).save(*args, **kwargs)

    def delete(self):
        """Check child and transaction relations."""
        return super(LayerOneModel, self).delete(related_object_name='layer_one_child')


class LayerTwoModel(LayersBaseModel):
    """This is the immedieate child class of the LayerOneModel."""

    parent_layer = models.ForeignKey(LayerOneModel, related_name='layer_one_child', verbose_name='Parent Layer', on_delete=models.CASCADE)
    created_by = models.ForeignKey(get_user_model(), related_name='layer_two_created_by', verbose_name='Created by', on_delete=models.CASCADE)

    class Meta(LayersBaseModel.Meta):
        """Meta data extending from parent Meta class."""

        db_table = str(DrfChartOfAccountConfig.name) + '_layer_two_table'
        verbose_name = 'Layer Two Model'
        verbose_name_plural = 'Layer Two Models'
        abstract = False

    def save(self, *args, **kwargs):
        """Set the ref_no and save the data to the model."""
        self.ref_no = str(uuid.uuid4())
        super(LayerTwoModel, self).save(*args, **kwargs)
        self.ref_no = self.get_ref_no(2)
        return super(LayerTwoModel, self).save(*args, **kwargs)

    def delete(self):
        """Check child and transaction relations."""
        return super(LayerTwoModel, self).delete(related_object_name='layer_two_child')


class LayerThreeModel(LayersBaseModel):
    """This is the immedieate child class of the LayerTwoModel."""

    parent_layer = models.ForeignKey(LayerTwoModel, related_name='layer_two_child', verbose_name='Parent Layer', on_delete=models.CASCADE)
    created_by = models.ForeignKey(get_user_model(), related_name='layer_three_created_by', verbose_name='Created by', on_delete=models.CASCADE)

    class Meta(LayersBaseModel.Meta):
        """Meta data extending from parent Meta class."""

        db_table = str(DrfChartOfAccountConfig.name) + '_layer_three_table'
        verbose_name = 'Layer Three Model'
        verbose_name_plural = 'Layer Three Models'
        abstract = False

    def save(self, *args, **kwargs):
        """Set the ref_no and save the data to the model."""
        self.ref_no = str(uuid.uuid4())
        super(LayerThreeModel, self).save(*args, **kwargs)
        self.ref_no = self.get_ref_no(3)
        return super(LayerThreeModel, self).save(*args, **kwargs)

    def delete(self):
        """Check child and transaction relations."""
        return super(LayerThreeModel, self).delete(related_object_name='layer_three_child')


class LayerFourModel(LayersBaseModel):
    """This is the immedieate child class of the LayerThreeModel."""

    parent_layer = models.ForeignKey(LayerThreeModel, related_name='layer_three_child', verbose_name='Parent Layer', on_delete=models.CASCADE)
    created_by = models.ForeignKey(get_user_model(), related_name='layer_four_created_by', verbose_name='Created by', on_delete=models.CASCADE)

    class Meta(LayersBaseModel.Meta):
        """Meta data extending from parent Meta class."""

        db_table = str(DrfChartOfAccountConfig.name) + '_layer_four_table'
        verbose_name = 'Layer Four Model'
        verbose_name_plural = 'Layer Four Models'
        abstract = False

    def save(self, *args, **kwargs):
        """Set the ref_no and save the data to the model."""
        self.ref_no = str(uuid.uuid4())
        super(LayerFourModel, self).save(*args, **kwargs)
        self.ref_no = self.get_ref_no(4)
        return super(LayerFourModel, self).save(*args, **kwargs)

    def delete(self):
        """Check child and transaction relations."""
        return super(LayerFourModel, self).delete(related_object_name='layer_four_child')


class LayerFiveModel(LayersBaseModel):
    """This is the immedieate child class of the LayerFourModel."""

    parent_layer = models.ForeignKey(LayerFourModel, related_name='layer_four_child', verbose_name='Parent Layer', on_delete=models.CASCADE)
    created_by = models.ForeignKey(get_user_model(), related_name='layer_five_created_by', verbose_name='Created by', on_delete=models.CASCADE)

    class Meta(LayersBaseModel.Meta):
        """Meta data extending from parent Meta class."""

        db_table = str(DrfChartOfAccountConfig.name) + '_layer_five_table'
        verbose_name = 'Layer Five Model'
        verbose_name_plural = 'Layer Five Models'
        abstract = False

    def save(self, *args, **kwargs):
        """Set the ref_no and save the data to the model."""
        self.ref_no = str(uuid.uuid4())
        super(LayerFiveModel, self).save(*args, **kwargs)
        self.ref_no = self.get_ref_no(5)
        return super(LayerFiveModel, self).save(*args, **kwargs)

    def delete(self):
        """Check child and transaction relations."""
        return super(LayerFiveModel, self).delete(related_object_name='layer_five_child')
