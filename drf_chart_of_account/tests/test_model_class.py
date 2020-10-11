"""Test cases for LayerModel classes."""
from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import (LayerOneModel, LayerTwoModel, LayerThreeModel,
                      LayerFourModel, LayerFiveModel)


class LayerModelClassesTestCases(TestCase):
    """Testing various methods of the Layer model class methods."""

    def setUp(self):
        """Construct the setup for the test cases."""
        test_user = get_user_model().objects.create(username='test_user_one', email='test_user_one@example.com', password='superacces123one')
        layer_one_obj_one = LayerOneModel(name='Layer one obj one', created_by=test_user)
        layer_one_obj_one.save()
        layer_one_obj_two = LayerOneModel(name='Layer one obj two', created_by=test_user)
        layer_one_obj_two.save()
        layer_two_object_one = LayerTwoModel(name='Layer two obj one', parent_layer=layer_one_obj_one, created_by=test_user)
        layer_two_object_one.save()
        layer_two_object_two = LayerTwoModel(name='Layer two obj two', parent_layer=layer_one_obj_two, created_by=test_user)
        layer_two_object_two.save()
        layer_three_object_one = LayerThreeModel(name='Layer three obj one', parent_layer=layer_two_object_one, created_by=test_user)
        layer_three_object_one.save()
        layer_three_object_two = LayerThreeModel(name='Layer three obj two', parent_layer=layer_two_object_two, created_by=test_user)
        layer_three_object_two.save()
        layer_four_object_one = LayerFourModel(name='Layer four obj one', parent_layer=layer_three_object_one, created_by=test_user)
        layer_four_object_one.save()
        layer_four_object_two = LayerFourModel(name='Layer four obj two', parent_layer=layer_three_object_two, created_by=test_user)
        layer_four_object_two.save()
        layer_five_object_one = LayerFiveModel(name='Layer five obj one', parent_layer=layer_four_object_one, created_by=test_user)
        layer_five_object_one.save()
        layer_five_object_two = LayerFiveModel(name='Layer five obj two', parent_layer=layer_four_object_two, created_by=test_user)
        layer_five_object_two.save()

    def test_layer_one_model_data(self):
        """Test LayerOneModel data."""
        layer_objects = LayerOneModel.objects.all()
        self.assertEqual(layer_objects[0].name, 'Layer one obj one')
        self.assertEqual(layer_objects[0].serial_no, 1)
        self.assertEqual(layer_objects[0].ref_no, '1.0.0.0.0')
        self.assertEqual(layer_objects[0].created_by.id, 1)
        self.assertEqual(layer_objects[1].name, 'Layer one obj two')
        self.assertEqual(layer_objects[1].serial_no, 2)
        self.assertEqual(layer_objects[1].ref_no, '2.0.0.0.0')
        self.assertEqual(layer_objects[1].created_by.id, 1)

    def test_layer_two_model_data(self):
        """Test LayerTwoModel data."""
        layer_objects = LayerTwoModel.objects.all()
        self.assertEqual(layer_objects[0].name, 'Layer two obj one')
        self.assertEqual(layer_objects[0].serial_no, 1)
        self.assertEqual(layer_objects[0].ref_no, '1.1.0.0.0')
        self.assertEqual(layer_objects[0].created_by.id, 1)
        self.assertEqual(layer_objects[1].name, 'Layer two obj two')
        self.assertEqual(layer_objects[1].serial_no, 2)
        self.assertEqual(layer_objects[1].ref_no, '2.1.0.0.0')
        self.assertEqual(layer_objects[1].created_by.id, 1)
