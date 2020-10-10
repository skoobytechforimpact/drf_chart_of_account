"""Test cases for ModuleConfigurations class."""
from django.test import TestCase
from django.core.exceptions import ValidationError
from ..configs import ModuleConfigurations


class ModuleConfigurationsTestCases(TestCase):
    """Testing various methods of the ModuleConfigurations class."""

    test_config_obj = ModuleConfigurations()

    def setUp(self):
        """Construct the setup for the test cases."""
        fake_settings_object_list = []
        fake_settings_object = type('test', (object,), {})()
        fake_settings_object_list.append(fake_settings_object)
        #  Setting DRF_CHART_OF_ACCOUNT keyword to the fake_settings_object
        fake_settings_object = type('test', (object,), {})()
        fake_settings_object.DRF_CA_CONFIGS = lambda: None
        setattr(fake_settings_object.DRF_CA_CONFIGS, 'DRF_CA_CONFIGS', {})
        fake_settings_object_list.append(fake_settings_object)
        fake_settings_object = type('test', (object,), {})()
        fake_settings_object.DRF_CA_CONFIGS = lambda: None
        setattr(fake_settings_object.DRF_CA_CONFIGS, 'DRF_CA_CONFIGS', {})
        fake_settings_object.DRF_CA_CONFIGS.DRF_CA_CONFIGS['reference_number_multiplayer'] = 'wrong data'
        fake_settings_object_list.append(fake_settings_object)
        fake_settings_object = type('test', (object,), {})()
        fake_settings_object.DRF_CA_CONFIGS = lambda: None
        setattr(fake_settings_object.DRF_CA_CONFIGS, 'DRF_CA_CONFIGS', {})
        fake_settings_object.DRF_CA_CONFIGS.DRF_CA_CONFIGS['reference_number_multiplayer'] = 100
        fake_settings_object_list.append(fake_settings_object)
        return fake_settings_object_list

    def test_check_variable_type_method(self):
        """Test check_variable_type method values."""
        self.assertRaisesMessage(ValidationError, 'variable cannot be None', self.test_config_obj.check_variable_type)
        self.assertRaisesMessage(ValidationError, 'variable cannot be None', self.test_config_obj.check_variable_type, type='test')
        self.assertRaisesMessage(ValidationError, 'type cannot be None', self.test_config_obj.check_variable_type, variable='test', type=None)
        self.assertEqual(self.test_config_obj.check_variable_type(2, int), True)
        self.assertEqual(self.test_config_obj.check_variable_type(2, str), False)

    def test_get_reference_number_multiplayer_method(self):
        """Test reference number multiplayer values."""
        test_settings_object_list = self.setUp()
        self.assertEqual(self.test_config_obj.get_reference_number_multiplayer(test_settings_object_list[0]), 10000)
        self.assertEqual(self.test_config_obj.get_reference_number_multiplayer(test_settings_object_list[1].DRF_CA_CONFIGS), 10000)
        self.assertRaisesMessage(ValidationError, 'reference_number_multiplayer must be integer type', self.test_config_obj.get_reference_number_multiplayer, settings_object=test_settings_object_list[2].DRF_CA_CONFIGS)
        self.assertEqual(self.test_config_obj.get_reference_number_multiplayer(test_settings_object_list[3].DRF_CA_CONFIGS), 100)
