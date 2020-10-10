"""Global classes or functions for this modules are here."""
from .configs import ModuleConfigurations


def reference_number_builder(layer_no=None, serial_no=0):
    """Make reference number based on layer number and serial number."""
    config_obj = ModuleConfigurations()
    return serial_no + config_obj.get_reference_number_multiplayer()
