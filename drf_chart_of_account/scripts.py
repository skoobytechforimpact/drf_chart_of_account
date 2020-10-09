"""Global classes or functions for this modules are here."""
from django.db.models import AutoField
from django.db.models.fields import checks
from .configs import ModuleConfigurations


class AutoFieldNonPrimaryKey(AutoField):
    """This subclass will raise Error if the AutoField primary_key is True."""

    def _check_primary_key(self):
        if self.primary_key:
            return [
                checks.Error(
                    "AutoFieldNonPrimaryKey must not set primary_key=True.",
                    obj=self,
                    id="fields.E100",
                )
            ]
        else:
            return []


def reference_number_builder(layer_no=None, serial_no=0):
    """Make reference number based on layer number and serial number."""
    config_obj = ModuleConfigurations()
    return serial_no + config_obj.get_reference_number_multiplayer()
