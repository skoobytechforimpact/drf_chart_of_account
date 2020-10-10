"""Handles the modules configuration values."""
from django.conf import settings
from django.core.exceptions import ValidationError


class ModuleConfigurations:
    """Holds and manages various configuration values for this module.

    Check if user defined configurations are present on the settings file if
    not then returns the system defined configuration values.
    """

    reference_number_multiplayer = 10000

    def check_variable_type(self, variable=None, type=None):
        """Raise error is variable and type is not matched."""
        if variable is None:
            raise ValidationError('variable cannot be None')
        if type is None:
            raise ValidationError('type cannot be None')
        if isinstance(variable, type):
            return True
        else:
            return False

    def get_reference_number_multiplayer(self, settings_object=None):
        """Search and return the reference_number_multiplayer value."""
        if settings_object is None:
            settings_object = settings
        else:
            settings_object = settings_object
        if hasattr(settings_object, 'DRF_CA_CONFIGS'):
            if 'reference_number_multiplayer' in settings_object.DRF_CA_CONFIGS:
                if self.check_variable_type(settings_object.DRF_CA_CONFIGS['reference_number_multiplayer'], int):
                    return settings_object.DRF_CA_CONFIGS['reference_number_multiplayer']
                else:
                    raise ValidationError('reference_number_multiplayer must be integer type')
            else:
                return self.reference_number_multiplayer
        else:
            return self.reference_number_multiplayer
