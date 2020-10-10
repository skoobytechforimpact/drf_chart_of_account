"""Chart of Accounts Layers Models and Classes."""
from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from .apps import DrfChartOfAccountConfig
import uuid


# Create your models here.
class LayersBaseModel(models.Model):
    """This is the abstract base class for all the layer models.

    All other layer model classes will extend this class. Only difference is
    the child layer class will override a foreign key relation key with it's
    parent class
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='ID')
    serial_no = models.IntegerField(null=False, blank=False, unique=True, verbose_name='Serial No.')
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

    def get_serial_no(self):
        """Calculate the serial number of the instance."""
        try:
            return self.__class__.objects.latest('serial_no').serial_no + 1
        except ObjectDoesNotExist:
            return 1

    def get_related_serial_no(self, parent_serial_no):
        """Calculate the related serial number against a parent layer serial number."""
        return self.__class__.objects.filter(parent_layer__serial_no=parent_serial_no).count() + 1

    def get_ref_no(self, layer_no):
        """Calculate the reference number of the instance."""
        if layer_no == 1:
            return str(self.serial_no) + '.0.0.0.0'
        elif layer_no == 2:
            return str(self.parent_layer.serial_no) + '.' + str(self.get_related_serial_no(self.parent_layer.serial_no)) + '.0.0.0'
        elif layer_no == 3:
            return str(self.parent_layer.parent_layer.serial_no) + '.' + str(self.parent_layer.serial_no) + '.' + str(self.get_related_serial_no(self.parent_layer.serial_no)) + '.0.0'
        elif layer_no == 4:
            return str(self.parent_layer.parent_layer.parent_layer.serial_no) + '.' + str(self.parent_layer.parent_layer.serial_no) + '.' + str(self.parent_layer.serial_no) + '.' + str(self.get_related_serial_no(self.parent_layer.serial_no)) + '.0'
        elif layer_no == 5:
            return str(self.parent_layer.parent_layer.parent_layer.parent_layer.serial_no) + '.' + str(self.parent_layer.parent_layer.parent_layer.serial_no) + '.' + str(self.parent_layer.parent_layer.serial_no) + '.' + str(self.parent_layer.serial_no) + '.' + str(self.get_related_serial_no(self.parent_layer.serial_no))
        else:
            raise ValidationError('layer no is not correct')


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
        self.serial_no = self.get_serial_no()
        self.ref_no = self.get_ref_no(1)
        return super(LayerOneModel, self).save(*args, **kwargs)


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
        self.serial_no = self.get_serial_no()
        self.ref_no = self.get_ref_no(2)
        return super(LayerTwoModel, self).save(*args, **kwargs)


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
        self.serial_no = self.get_serial_no()
        self.ref_no = self.get_ref_no(3)
        return super(LayerThreeModel, self).save(*args, **kwargs)


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
        self.serial_no = self.get_serial_no()
        self.ref_no = self.get_ref_no(4)
        return super(LayerFourModel, self).save(*args, **kwargs)


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
        self.serial_no = self.get_serial_no()
        self.ref_no = self.get_ref_no(5)
        return super(LayerFiveModel, self).save(*args, **kwargs)
