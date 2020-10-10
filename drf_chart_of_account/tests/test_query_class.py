"""Test cases for ParentLayerQueryClass class."""
from django.test import TestCase
from django.contrib.auth import get_user_model
from ..queries import ParentLayerQueryClass
from ..models import (LayerOneModel, LayerTwoModel, LayerThreeModel,
                      LayerFourModel, LayerFiveModel)


class ParentLayerQueryClassTestCases(TestCase):
    """Testing various methods of the ParentLayerQueryClass methods."""

    test_obj = ParentLayerQueryClass()

    def setUp(self):
        """Construct the setup for the test cases."""
        test_user = get_user_model().objects.create(username='test_user_one', email='test_user_one@example.com', password='superacces123one')
        layer_one_obj_one = LayerOneModel(serial_no=1, name='Layer one obj one', created_by=test_user)
        layer_one_obj_one.save()
        layer_one_obj_two = LayerOneModel(serial_no=2, name='Layer one obj two', created_by=test_user)
        layer_one_obj_two.save()
        layer_two_object_one = LayerTwoModel(serial_no=1, name='Layer two obj one', parent_layer=layer_one_obj_one, created_by=test_user)
        layer_two_object_one.save()
        layer_two_object_two = LayerTwoModel(serial_no=2, name='Layer two obj two', parent_layer=layer_one_obj_two, created_by=test_user)
        layer_two_object_two.save()
        layer_three_object_one = LayerThreeModel(serial_no=1, name='Layer three obj one', parent_layer=layer_two_object_one, created_by=test_user)
        layer_three_object_one.save()
        layer_three_object_two = LayerThreeModel(serial_no=2, name='Layer three obj two', parent_layer=layer_two_object_two, created_by=test_user)
        layer_three_object_two.save()
        layer_four_object_one = LayerFourModel(serial_no=1, name='Layer four obj one', parent_layer=layer_three_object_one, created_by=test_user)
        layer_four_object_one.save()
        layer_four_object_two = LayerFourModel(serial_no=2, name='Layer four obj two', parent_layer=layer_three_object_two, created_by=test_user)
        layer_four_object_two.save()
        layer_five_object_one = LayerFiveModel(serial_no=1, name='Layer five obj one', parent_layer=layer_four_object_one, created_by=test_user)
        layer_five_object_one.save()
        layer_five_object_two = LayerFiveModel(serial_no=2, name='Layer five obj two', parent_layer=layer_four_object_two, created_by=test_user)
        layer_five_object_two.save()

    def test_empty_values_to_the_list(self):
        """Test insert_empty_value_to_list method."""
        self.assertEqual(self.test_obj.insert_empty_value_to_list(loop_no=0), [])
        self.assertEqual(self.test_obj.insert_empty_value_to_list(loop_no=1), [0])
        self.assertEqual(self.test_obj.insert_empty_value_to_list(loop_no=2), [0, 0, 0])

    def test_layer_two_query(self):
        """Test layer two query method."""
        self.assertEqual(self.test_obj.layer_two_query(serial_no=1), [1, 1, 0, 0, 0])
        self.assertEqual(self.test_obj.layer_two_query(serial_no=2), [2, 2, 0, 0, 0])

    def test_layer_three_query(self):
        """Test layer three query method."""
        self.assertEqual(self.test_obj.layer_three_query(serial_no=1), [1, 1, 1, 0, 0])
        self.assertEqual(self.test_obj.layer_three_query(serial_no=2), [2, 2, 2, 0, 0])

    def test_layer_four_query(self):
        """Test layer four query method."""
        self.assertEqual(self.test_obj.layer_four_query(serial_no=1), [1, 1, 1, 1, 0])
        self.assertEqual(self.test_obj.layer_four_query(serial_no=2), [2, 2, 2, 2, 0])

    def test_layer_five_query(self):
        """Test layer five query method."""
        self.assertEqual(self.test_obj.layer_five_query(serial_no=1), [1, 1, 1, 1, 1])
        self.assertEqual(self.test_obj.layer_five_query(serial_no=2), [2, 2, 2, 2, 2])
