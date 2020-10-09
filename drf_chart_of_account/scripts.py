"""Global classes or functions for this modules are here."""
from django.db.models import AutoField
from django.db.models.fields import checks


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
